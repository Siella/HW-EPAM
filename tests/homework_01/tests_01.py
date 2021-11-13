import os

from homework_01.hw1 import (count_non_ascii_chars, count_punctuation_chars,
                             get_longest_diverse_words,
                             get_most_common_non_ascii_char, get_rarest_char)


def test_sample():
    def find(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
    sample = find('par_1.txt', os.getcwd())
    assert set(get_longest_diverse_words(sample)) == {
        'Betrachtung', 'bedenklichen', 'hinausführen',
        'vorgebahnte', 'Waldgang', 'vielmehr', 'verbirgt',
        'Ausflug', 'hinter', 'gefaßt'}, 'Fail 1'
    assert get_rarest_char(sample) == 'W', 'Fail 2'
    assert count_punctuation_chars(sample) == 8, 'Fail 3'
    assert count_non_ascii_chars(sample) == 6, 'Fail 4'
    assert get_most_common_non_ascii_char(sample) == 'ü', 'Fail 5'
