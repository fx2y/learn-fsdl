from pathlib import Path

import numpy as np

from text_recognizer.datasets.dataset import Dataset

DATA_DIRNAME = Dataset.data_dirname() / 'processed' / 'emnist_lines'
ESSENTIALS_FILENAME = Path(__file__).parents[0].resolve() / 'emnist_lines_essentials.json'


class EmnistLinesDataset(Dataset):
    def __init__(self, max_length: int = 34, max_overlap: float = 0.33, num_train: int = 10000, num_test: int = 1000):
        pass

    @property
    def data_filename(self):
        pass

    def load_or_generate_data(self):
        pass

    def __repr__(self):
        pass

    def _load_data(self):
        pass

    def _generate_data(self, split):
        pass


def get_samples_by_char(samples, labels, mapping):
    pass


def select_letter_samples_for_string(string, samples_by_char):
    pass


def construct_image_from_string(string: str, samples_by_char: dict, max_oerlap: float) -> np.ndarray:
    pass


def create_dataset_of_images(N, samples_by_char, sentence_generator, max_overlap):
    pass


def convert_strings_to_categorical_labels(labels, mapping):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
