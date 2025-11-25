# test/test_engine.py

import unittest
import os
import sys

# --- PERBAIKAN IMPORT PATH ---
# Menambahkan direktori induk (Kersey_MBTI) ke Python path (sys.path).
# Ini penting agar Python dapat menemukan package 'engine' dan 'utils'.
# os.path.dirname(__file__) -> direktori 'test'
# os.path.dirname(os.path.dirname(__file__)) -> direktori 'Kersey_MBTI'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import sekarang seharusnya bekerja
from engine.fuzzy_engine import FuzzyEngine

class TestFuzzyEngine(unittest.TestCase):

    def setUp(self):
        # Asumsikan file CSV berada di Kersey_MBTI/data/
        # Karena kita menjalankan dari folder 'test', kita perlu path relatif yang benar
        self.engine = FuzzyEngine("data/keirsey_mbtifuzzy_70q.csv") # Naik satu level ke 'Kersey_MBTI' lalu masuk ke 'data'

    def test_single_answer(self):
        # ... (sisanya sama)
        self.engine.answer(1, 'a')
        result = self.engine.finalize()
        self.assertTrue(len(result) == 4)

    def test_multiple_answers(self):
        # ... (sisanya sama)
        self.engine.answer(1, 'a')
        self.engine.answer(2, 'b')
        self.engine.answer(3, 'a')
        result = self.engine.finalize()
        self.assertTrue(len(result) == 4)

if __name__ == "__main__":
    unittest.main()