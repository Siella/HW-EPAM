import os

import pytest

from homework9.hw1 import merge_sorted_files

content = [
    '3\n1\n2',
    '4\n6\n5',
    '',
]


@pytest.fixture
def create_test_files():
    file_list = []
    for i, cont in enumerate(content):
        with open(f"test_{i}.txt", "w+") as f:
            f.write(cont)
        file_list.append(f"test_{i}.txt")
    yield file_list
    for f in file_list:
        os.remove(f)


def test_merge_sorted_files(create_test_files):
    assert list(merge_sorted_files(
        create_test_files
    )) == [1, 2, 3, 4, 5, 6]
