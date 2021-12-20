import pytest

from homework9.hw2 import SuppressorClass, context_manager_suppressor


def test_suppressor():
    with SuppressorClass(IndexError):
        [][2]

    with context_manager_suppressor(IndexError):
        [][2]

    with pytest.raises(IndexError) as excinfo:
        with SuppressorClass(ValueError):
            [][2]
    assert issubclass(excinfo.type, IndexError)

    with pytest.raises(IndexError) as excinfo:
        with context_manager_suppressor(ValueError):
            [][2]
    assert issubclass(excinfo.type, IndexError)
