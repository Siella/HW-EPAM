"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from itertools import product
from typing import Any, List


def lists_combinations(*args: List[Any]) -> List[List]:
    combinations = [comb for comb in product(*args)]
    return list(map(list, combinations))


if __name__ == '__main__':
    print(lists_combinations([1, 2], [3, 4]))
    print(lists_combinations([1, 2], [3], [4]))
    print(lists_combinations([1, 2], [3], [5, 6]))
    print(lists_combinations([1, 2], [1, 2]))
