"""SentenceGenerator class and supporting functions."""
from typing import Optional

from text_recognizer.datasets.dataset import Dataset

NLTK_DATA_DIRNAME = Dataset.data_dirname() / 'raw' / 'nltk'


class SentenceGenerator:
    """Generate text sentences using the Brown corpus."""

    def __init__(self, max_length: Optional[int] = None):
        pass

    def generate(self, max_length: Optional[int] = None) -> str:
        pass


def brown_text():
    pass


def load_nltk_brown_corpus():
    pass
