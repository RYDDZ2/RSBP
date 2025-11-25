# utils/__init__.py

from .csv_loader import CSVLoader
from .question_loader import QuestionLoader # Mengasumsikan Anda sudah membuat question_loader.py

# Kita bisa mendefinisikan apa yang diekspor ketika 'import *' digunakan
__all__ = [
    "CSVLoader",
    "QuestionLoader"
]