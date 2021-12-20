import os
from pathlib import Path

import pytest

from homework9.hw3 import universal_file_counter

content = [
    '3\n1\n2',
    '4 2\n6\n5 9',
    '',
]


@pytest.fixture
def create_test_files():
    file_list = []
    for i, cont in enumerate(content):
        with open(f"test_{i}.txt", "w+") as f:
            f.write(cont)
        file_list.append(f"test_{i}.txt")
    yield Path.cwd()
    for f in file_list:
        os.remove(f)


def test_universal_file_counter(create_test_files):
    assert universal_file_counter(create_test_files) == 6
    assert universal_file_counter(create_test_files, tokenizer=str.split) == 8
