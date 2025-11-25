# engine/model.py

class PersonalityModel:
    # TRAIT_KEYS sekarang mencakup 8 MBTI Traits dan 4 Keirsey Traits
    TRAIT_KEYS = [
        "E", "I", 
        "S", "N", 
        "T", "F", 
        "J", "P",
        "A", "G", "I_temp", "R" # A=Artisan, G=Guardian, I_temp=Idealist, R=Rational
    ]
    
    # Mapping Keirsey (Hanya untuk referensi, klasifikasi akan menggunakan fuzzy score)
    KEIRSEY_MAP = {
        'A': 'Artisan (SP)', 
        'G': 'Guardian (SJ)', 
        'I_temp': 'Idealist (NF)', 
        'R': 'Rational (NT)',
    }

    def __init__(self):
        self.scores = {k: 0.0 for k in self.TRAIT_KEYS}
        self.answered = 0

    def apply_scores(self, scores_dict):
        """
        Tambahkan skor trait ke akumulasi, termasuk skor Keirsey.
        """
        for trait, value in scores_dict.items():
            if trait in self.scores:
                self.scores[trait] += value

        self.answered += 1

    def get_mbti(self):
        """
        Tentukan MBTI 4-huruf dari skor total fuzzy.
        E vs I, S vs N, T vs F, J vs P
        """
        result = ""
        result += "E" if self.scores["E"] >= self.scores["I"] else "I"
        result += "S" if self.scores["S"] >= self.scores["N"] else "N"
        result += "T" if self.scores["T"] >= self.scores["F"] else "F"
        result += "J" if self.scores["J"] >= self.scores["P"] else "P"
        
        return result

    def get_keirsey_temperament(self):
        """
        Tentukan 4 Temperamen Keirsey berdasarkan bobot fuzzy (A, G, I_temp, R) tertinggi.
        """
        keirsey_traits = ['A', 'G', 'I_temp', 'R']
        
        # Cari trait Keirsey dengan skor tertinggi
        max_score = -1.0
        best_trait = None
        
        for trait in keirsey_traits:
            score = self.scores[trait]
            if score > max_score:
                max_score = score
                best_trait = trait
            # Penanganan kasus seri (tie) bisa ditambahkan jika diperlukan
            
        return self.KEIRSEY_MAP.get(best_trait, "Temperamen Tidak Dikenal")

    def get_keirsey_fuzzy_scores(self):
        """
        Mengembalikan bobot fuzzy untuk 4 temperamen Keirsey.
        """
        keirsey_traits = ['A', 'G', 'I_temp', 'R']
        
        keirsey_scores = {
            self.KEIRSEY_MAP[trait]: self.scores[trait]
            for trait in keirsey_traits
        }
        return keirsey_scores

    def get_score_report(self):
        """Mengembalikan semua skor mentah (MBTI + Keirsey)."""
        return self.scores