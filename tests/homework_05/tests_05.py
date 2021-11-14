import string

from homework_05.hw5 import custom_range


def test_custom_range():
    assert custom_range(string.ascii_lowercase, 'g') == \
           ['a', 'b', 'c', 'd', 'e', 'f']
    assert custom_range(string.ascii_lowercase, 'g', 'p') == \
           ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == \
           ['p', 'n', 'l', 'j', 'h']
