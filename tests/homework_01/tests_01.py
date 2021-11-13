import os

from homework_01.hw1 import (count_non_ascii_chars, count_punctuation_chars,
                             get_longest_diverse_words,
                             get_most_common_non_ascii_char, get_rarest_char)


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


sample = find('par_1.txt', os.getcwd())


def test_get_longest_diverse_words():
    assert set(get_longest_diverse_words(sample)) == {
        'Betrachtung', 'bedenklichen', 'hinausf\u00fchren',
        'vorgebahnte', 'Waldgang', 'vielmehr', 'verbirgt',
        'Ausflug', 'hinter', 'gefa\u00dft'}, 'Fail 1'


def test_get_rarest_char():
    assert get_rarest_char(sample) == 'W', 'Fail 2'


def test_count_punctuation_chars():
    assert count_punctuation_chars(sample) == 8, 'Fail 3'


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(sample) == 6, 'Fail 4'


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(sample) == '\u00fc', 'Fail 5'
