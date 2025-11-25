from flask import Flask, render_template, jsonify
import os
import sys

# Tambahkan path agar modul engine dan utils terbaca
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from engine.fuzzy_engine import FuzzyEngine
from utils.question_loader import QuestionLoader

app = Flask(__name__)

# Konfigurasi Path File CSV
CSV_SKOR = "data/keirsey_mbtifuzzy_70q.csv"
CSV_TANYA = "data/questions.csv"

@app.route('/')
def home():
    """Menampilkan halaman Frontend (HTML)"""
    return render_template('index.html')

@app.route('/api/get-quiz-data')
def get_quiz_data():
    """
    API ini mengambil data dari Python Backend dan mengirimnya ke Frontend.
    Menggabungkan pertanyaan (teks) dengan bobot skor (fuzzy logic).
    """
    try:
        # 1. Load Data menggunakan script teman Anda
        engine = FuzzyEngine(CSV_SKOR) # Memuat bobot skor
        q_loader = QuestionLoader(CSV_TANYA) # Memuat teks pertanyaan
        
        # Ambil raw data
        all_questions_text = q_loader.load_questions() # Dictionary {1: {'pertanyaan':...}, ...}
        all_scores_data = engine.questions # Dictionary {1: [{'option': 'a', 'scores':...}], ...}
        
        # 2. Gabungkan menjadi format JSON yang bersih untuk Frontend
        quiz_data = []
        
        # Kita looping sebanyak jumlah pertanyaan
        total_q = len(all_questions_text)
        
        for i in range(1, total_q + 1):
            if i in all_questions_text and i in all_scores_data:
                q_text = all_questions_text[i]
                q_score = all_scores_data[i]
                
                # Cari skor untuk opsi A dan B
                score_a = next((item['scores'] for item in q_score if item['option'] == 'a'), {})
                score_b = next((item['scores'] for item in q_score if item['option'] == 'b'), {})
                
                quiz_data.append({
                    "q": i,
                    "text": q_text['pertanyaan'],
                    "a": q_text['opsi_a'],
                    "b": q_text['opsi_b'],
                    "scoresA": score_a, # Backend mengirim logika hitungan ke frontend
                    "scoresB": score_b
                })
                
        return jsonify(quiz_data)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)