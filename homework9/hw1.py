"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


class InvalidNumberError(Exception):
    pass


class MyFileIter:
    def __init__(self, file_list: List[Union[Path, str]]):
        self.file_list = file_list
        self.data = self.merge_and_sort()
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        i = self._index
        self._index += 1
        if self._index <= len(self.data):
            return self.data[i]
        else:
            raise StopIteration

    def merge_and_sort(self, encoding='utf-8'):
        data = []
        for file in self.file_list:
            with open(file, encoding=encoding) as f:
                for line in f.readlines():
                    try:
                        element = int(line)
                    except ValueError:
                        raise InvalidNumberError(
                            'File must contain only integers!'
                        )
                    data.append(element)
        data.sort()
        return data


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    return MyFileIter(file_list)


if __name__ == '__main__':
    print(list(merge_sorted_files(["file1.txt", "file2.txt"])))
