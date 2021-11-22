import os
from unittest.mock import mock_open, patch

import pytest

from task_01.task_1_read_file import read_magic_number


def test_invalid_path():
    fake_path = f'{os.getcwd()}\\no_existing_file.txt'
    with pytest.raises(ValueError) as excinfo:
        read_magic_number(fake_path)
    assert "Can't find or read a file" in str(excinfo.value)


@patch("builtins.open", new_callable=mock_open, read_data="not_float_value")
def test_invalid_value(mock):
    with pytest.raises(ValueError) as excinfo:
        read_magic_number(".gitignore")
    assert "Can't convert data to a float" in str(excinfo.value)


@patch("builtins.open", new_callable=KeyError)
def test_unexpected_behaviour(mock):
    with pytest.raises(ValueError) as excinfo:
        read_magic_number(".gitignore")
    assert "Unexpected error 'KeyError'" in str(excinfo.value)


def test_existing_file_with_valid_number():
    with open('good_file.txt', 'w') as f:
        f.write('1')
    assert read_magic_number("good_file.txt") is True
    os.remove("good_file.txt")
