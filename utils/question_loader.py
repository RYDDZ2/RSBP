import csv

class QuestionLoader:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def load_questions(self):
        """
        Load pertanyaan dari questions.csv (teks pertanyaan dan opsi A/B).
        """
        questions = {}
        
        try:
            with open(self.csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    # Pastikan 'q' ada dan bisa dikonversi ke integer
                    if 'q' not in row or not row['q'].isdigit():
                        continue
                        
                    q_number = int(row['q'])
                    questions[q_number] = {
                        "pertanyaan": row.get('Pertanyaan', 'N/A'),
                        "opsi_a": row.get('Opsi_A', 'N/A'),
                        "opsi_b": row.get('Opsi_B', 'N/A')
                    }
        except FileNotFoundError:
            print(f"Error: File pertanyaan tidak ditemukan di {self.csv_path}")
            return {}
        except Exception as e:
            print(f"Error saat memuat pertanyaan: {e}")
            return {}

        return questions