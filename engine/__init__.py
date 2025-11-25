# engine/__init__.py

from .fuzzy_engine import FuzzyEngine
from .model import PersonalityModel

# Kita bisa mendefinisikan apa yang diekspor ketika 'import *' digunakan
__all__ = [
    "FuzzyEngine",
    "PersonalityModel"
]