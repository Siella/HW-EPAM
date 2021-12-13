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


def custom_range(iter_object: Sequence[Any], *args) -> List[Any]:
    """
    If given one argument in args, it will be considered as a stop element.
    If given two or three arguments, then it'll be treated as start, stop[, step].
    :param iter_object: an iterable object to create range
    :param args: stop | start, stop[, step]
    :return:
    """
    if len(args) == 1:
        start, stop, step = None, args[0], 1
    if len(args) == 2:
        start, stop, step = args[0], args[1], 1
    if len(args) > 2:
        start, stop, step = args[0], args[1], args[2]

    list_ = list(iter_object)
    start_with, end_by = 0, len(list_)
    if start is not None:
        start_with, end_by = list_.index(start), list_.index(stop)
    else:
        end_by = list_.index(stop)
    return list_[start_with:end_by:step]
