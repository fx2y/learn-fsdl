"""Utility functions for text_recognizer module."""
import hashlib
from pathlib import Path
from typing import Union
from urllib.request import urlretrieve

import numpy as np
from tqdm import tqdm


def read_image(image_uri: Union[Path, str], grayscale=False) -> np.array:
    """Read image_uri."""

    def read_image_from_filename(image_filename, imread_flag):
        pass

    def read_image_from_url(image_url, imread_flag):
        pass


def read_b64_image(b64_string, grayscale=False):
    pass


def write_image(image: np.ndarray, filename: Union[Path, str]) -> None:
    pass


def compute_sha256(filename: Union[Path, str]):
    """Return SHA256 checksum of a file."""
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


class TqdmUpTo(tqdm):
    """From https://github.com/tqdm/tqdm/blob/master/examples/tqdm_wget.py"""

    def update_to(self, blocks=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(blocks * bsize - self.n)


def download_url(url, filename):
    """Download a file from url to filename, with a progress bar."""
    with TqdmUpTo(unit='B', unit_scale=True, unit_divisor=1024, miniters=1) as t:
        urlretrieve(url, filename, reporthook=t.update_to, data=None)


def download_urls(urls, filename):
    pass
