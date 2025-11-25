# utils/csv_loader.py

import csv

class CSVLoader:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def load_questions(self):
        """
        Load seluruh baris dari CSV dan kelompokkan berdasarkan nomor pertanyaan.
        """
        questions = {}

        try:
            with open(self.csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    if 'q' not in row or 'option' not in row or not row['q'].isdigit():
                        continue

                    q_number = int(row['q'])
                    option = row['option']

                    # Trait scoring diambil otomatis kolom selain q & option
                    # Cek apakah nilai bisa dikonversi ke float sebelum dimasukkan
                    scores = {
                        key: float(value)
                        for key, value in row.items()
                        if key not in ['q', 'option'] and value.replace('.', '', 1).isdigit()
                    }

                    if q_number not in questions:
                        questions[q_number] = []

                    questions[q_number].append({
                        "option": option,
                        "scores": scores
                    })
        except FileNotFoundError:
            print(f"Error: File CSV tidak ditemukan di {self.csv_path}")
            return {}
        except Exception as e:
            print(f"Error saat memuat CSV: {e}")
            return {}

        return questions