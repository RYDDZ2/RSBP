# engine/fuzzy_engine.py

from utils.csv_loader import CSVLoader
from .model import PersonalityModel

class FuzzyEngine:
    def __init__(self, csv_path):
        self.loader = CSVLoader(csv_path)
        self.questions = self.loader.load_questions()
        self.model = PersonalityModel()

    def answer(self, q_number, chosen_option):
        """
        User menjawab satu pertanyaan.
        """
        if q_number not in self.questions:
            raise ValueError(f"Pertanyaan Q{q_number} tidak ditemukan.")

        options = self.questions[q_number]
        
        # Cari row CSV yang sesuai pilihan user
        match = next(
            (opt for opt in options if opt["option"] == chosen_option.lower()),
            None
        )

        if match is None:
            raise ValueError(f"Pilihan tidak valid '{chosen_option}' untuk Q{q_number}")

        # Apply skor fuzzy ke model (Skor ini mencakup MBTI dan Keirsey)
        self.model.apply_scores(match["scores"])

    def finalize(self):
        """Generate MBTI final."""
        return self.model.get_mbti()

    def debug_report(self):
        """Lihat semua skor mentah."""
        return self.model.get_score_report()