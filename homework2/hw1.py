"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import re
from collections import defaultdict
from typing import List


def read_by_lines(
        file_path: str, encoding='unicode-escape', errors='ignore'
        ) -> str:
    with open(file_path, 'r', encoding=encoding, errors=errors) as f:
        for line in f:
            yield line
        return


def is_non_ascii(char):
    return ord(char) > 126  # without extended


def get_longest_diverse_words(
        file_path: str, encoding='unicode-escape', errors='ignore'
        ) -> List[str]:
    def clear_punc_num_chars(word):
        new_word = re.sub(r'[^\w\s]', '', word)
        new_word = re.sub(r'\d+', '', new_word)
        return new_word
    words_dict = dict()  # key is a word, value is a num of unique symbols
    concat_words, last_part = False, ''  # for word wrap cases
    for line in read_by_lines(file_path, encoding, errors):
        new_line = line[:]
        if concat_words:
            new_line = last_part + line
            concat_words = False
        if line.find('-\n') != -1:
            last_part_idx = line.rfind(' ')+1
            last_part = line[last_part_idx:-2]
            new_line = line[:last_part_idx]
            concat_words = True
        words_per_line = list(map(clear_punc_num_chars, new_line.split()))
        words_dict.update({w: len(set(w)) for w in words_per_line})
    return sorted(words_dict, key=words_dict.get, reverse=True)[:10]


def get_rarest_char(
        file_path: str, encoding='unicode-escape', errors='ignore'
        ) -> str:
    char_dict = defaultdict(int)  # key is a char, value - num of occurrences
    for line in read_by_lines(file_path, encoding, errors):
        for char in line:
            char_dict[char] += 1
    return min(char_dict, key=char_dict.get)


def count_punctuation_chars(
        file_path: str, encoding='unicode-escape', errors='ignore'
        ) -> int:
    cnt_punc = 0
    for line in read_by_lines(file_path, encoding, errors):
        cnt_punc += len(line) - len(re.sub(r'[^\w\s]', '', line))
    return cnt_punc


def count_non_ascii_chars(
        file_path: str, encoding='unicode-escape', errors='ignore') -> int:
    cnt_non_ascii = 0
    for line in read_by_lines(file_path, encoding, errors):
        cnt_non_ascii += sum(list(map(is_non_ascii, line)))
    return cnt_non_ascii


def get_most_common_non_ascii_char(
        file_path: str, encoding='unicode-escape', errors='ignore'
        ) -> str:
    char_dict = defaultdict(int)
    for line in read_by_lines(file_path, encoding, errors):
        new_line = list(filter(is_non_ascii, line))
        for char in new_line:
            char_dict[char] += 1
    return max(char_dict, key=char_dict.get)


if __name__ == "__main__":
    print(get_longest_diverse_words('data.txt'))
    print(get_rarest_char('data.txt'))
    print(count_punctuation_chars('data.txt'))
    print(count_non_ascii_chars('data.txt'))
    print(get_most_common_non_ascii_char('data.txt'))
