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
    # n is for case of different lengths of lists
    K, n = len(args), max(list(map(len, args)))
    result = []
    for indices in product(range(n), repeat=K):
        tmp_result = []
        to_add = True
        for i, idx in enumerate(indices):
            if idx < len(args[i]):
                tmp_result += [args[i][idx]]
            else:
                to_add = False
                break
        if to_add:
            result += [tmp_result]
    return result


if __name__ == '__main__':
    print(lists_combinations([1, 2], [3, 4]))
    print(lists_combinations([1, 2], [3], [4]))
    print(lists_combinations([1, 2], [3], [5, 6]))
    print(lists_combinations([1, 2], [1, 2]))
