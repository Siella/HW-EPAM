"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert custom_range(string.ascii_lowercase, 'g') ==
        ['a', 'b', 'c', 'd', 'e', 'f']
assert custom_range(string.ascii_lowercase, 'g', 'p') ==
        ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
        ['p', 'n', 'l', 'j', 'h']

"""
from collections.abc import Iterable
from typing import Any, List


def custom_range(iter_object: Iterable[Any],
                 start: Any = None,
                 end: Any = None,
                 step: int = 1) -> List[Any]:
    list_ = list(iter_object)
    start_with, end_by = 0, len(list_)
    if (start is not None) & (end is None):
        end_by = list_.index(start)
    elif end is not None:
        start_with = list_.index(start)
        end_by = list_.index(end)
    return list_[start_with:end_by:step]
