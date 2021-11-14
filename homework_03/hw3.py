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
from itertools import chain, combinations
from typing import Any, List


def lists_combinations(*args: List[Any]) -> List[List]:
    n = min(list(map(len, args)))  # in case of different lengths of lists
    values = list(chain(*args))
    all_comb = combinations(values, n)
    exclude_combs = list(chain(*[list(combinations(l_[:n], n))
                                 for l_ in args]))
    result = list(filter(lambda x: x not in exclude_combs, all_comb))
    return list(map(list, result))


if __name__ == '__main__':
    print(lists_combinations([1, 2], [3, 4]))
    print(lists_combinations([0, 1, 2], [3, 4, 5], [6, 7, 8]))
    print(lists_combinations([0, 1], [2, 3, 4], [5, 6]))
