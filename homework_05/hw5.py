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
from typing import Any, List, Sequence


def custom_range(iter_object: Sequence[Any],
                 end: Any,  # mandatory argument
                 start: Any = None,
                 step: int = 1) -> List[Any]:
    list_ = list(iter_object)
    start_with, end_by = 0, len(list_)
    if start is not None:
        start_with, end_by = list_.index(end), list_.index(start)
    else:
        end_by = list_.index(end)
    return list_[start_with:end_by:step]
