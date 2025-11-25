# main.py

import os
import sys

# Tambahkan direktori root agar import berfungsi
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from engine.fuzzy_engine import FuzzyEngine
from utils.question_loader import QuestionLoader

# --- Konfigurasi File ---
SKOR_CSV_PATH = "data/keirsey_mbtifuzzy_70q.csv"
PERTANYAAN_CSV_PATH = "data/questions.csv"

def run_assessment():
    """
    Menjalankan proses kuesioner Keirsey-MBTI.
    """
    print("=========================================")
    print(" Sistem Pakar Keirsey-MBTI (Fuzzy Logic) ")
    print("=========================================")

    # 1. Inisialisasi Engine dan Loader
    try:
        engine = FuzzyEngine(SKOR_CSV_PATH)
        q_loader = QuestionLoader(PERTANYAAN_CSV_PATH)
        all_questions = q_loader.load_questions()
    except Exception as e:
        print(f"\n[FATAL] Gagal inisialisasi: {e}")
        return

    if not all_questions:
        print("\n[FATAL] Tidak ada pertanyaan yang dimuat. Periksa file CSV.")
        return

    total_questions = len(all_questions)
    print(f"\n💡 Kuesioner siap. Total {total_questions} pertanyaan.\n")

    # 2. Loop Pertanyaan dan Kumpulkan Jawaban
    for q_number in range(1, total_questions + 1):
        if q_number not in all_questions:
            print(f"Warning: Q{q_number} hilang dari file pertanyaan.")
            continue
            
        q_data = all_questions[q_number]
        
        print(f"--- Pertanyaan {q_number}/{total_questions} ---")
        print(f"{q_data['pertanyaan']}")
        print(f"A. {q_data['opsi_a']}")
        print(f"B. {q_data['opsi_b']}")
        
        while True:
            choice = input("Pilih (A/B): ").strip().upper()
            if choice in ['A', 'B']:
                try:
                    engine.answer(q_number, choice.lower())
                    print("Jawaban tersimpan.\n")
                    break
                except ValueError as ve:
                    print(f"[Error Engine] {ve}. Coba lagi.")
                    
            else:
                print("Pilihan tidak valid. Silakan pilih A atau B.")
    
    # 3. Finalisasi dan Tampilkan Hasil
    print("\n=========================================")
    print("✅ Semua pertanyaan terjawab. Menghitung hasil...")
    
    try:
        final_mbti = engine.finalize()
        # Panggil klasifikasi Keirsey berbasis Fuzzy Score
        final_keirsey = engine.model.get_keirsey_temperament() 
        score_report = engine.debug_report()
        keirsey_fuzzy_scores = engine.model.get_keirsey_fuzzy_scores() 

        # --- OUTPUT UTAMA ---
        print("\n=========================================")
        print(f"📊 Hasil Tipe Kepribadian")
        print("=========================================")
        print(f"  Tipe MBTI (16 Tipe)   : **{final_mbti}**")
        print(f"  Temperamen Keirsey    : **{final_keirsey}**")
        print("=========================================")
        
        # --- OUTPUT BOBOT KEIRSEY FUZZY ---
        print("\n--- Bobot Fuzzy 4 Temperamen Keirsey ---")
        
        # Cari skor Keirsey tertinggi untuk visualisasi
        sorted_keirsey = sorted(keirsey_fuzzy_scores.items(), key=lambda item: item[1], reverse=True)
        
        for temperament, score in sorted_keirsey:
            # Highlight yang terpilih
            is_winner = "(*TERPILIH*)" if temperament == final_keirsey else ""
            print(f" {temperament:<20}: {score:7.3f} {is_winner}")
        
        # --- OUTPUT DETAIL SKOR MBTI FUZZY ---
        print("\n--- Detail Bobot Fuzzy MBTI (8 Traits) ---")
        # Hanya tampilkan 8 traits MBTI (E/I, S/N, T/F, J/P)
        mbti_traits = score_report.keys() - keirsey_fuzzy_scores.keys()
        sorted_mbti_scores = {k: score_report[k] for k in sorted(score_report.keys()) if k in ['E', 'I', 'S', 'N', 'T', 'F', 'J', 'P']}
        
        i = 0
        for trait, score in sorted_mbti_scores.items():
            print(f" {trait}: {score:7.3f}", end=" | " if (i+1) % 2 == 0 else " ")
            i += 1
        print("\n")

    except Exception as e:
        print(f"\n[FATAL] Gagal menghitung hasil: {e}")


if __name__ == "__main__":
    if not os.path.isdir('data'):
        print("Direktori 'data' tidak ditemukan. Harap buat dan letakkan file CSV di sana.")
    else:
        if os.path.exists(SKOR_CSV_PATH) and os.path.exists(PERTANYAAN_CSV_PATH):
            run_assessment()
        else:
            print("File CSV data/keirsey_mbtifuzzy_70q.csv atau data/questions.csv tidak ditemukan.")