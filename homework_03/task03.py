"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    first = True
    with open(file_name) as f:
        for line in f:
            curr_elem = int(line)
            if first:
                max_elem = curr_elem
                min_elem = curr_elem
                first = False
                continue
            if curr_elem > max_elem:
                max_elem = curr_elem
            if curr_elem < min_elem:
                min_elem = curr_elem
        if first:
            print('An empty file!')
            return -1, -1
    return min_elem, max_elem