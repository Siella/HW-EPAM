"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fib(data: Sequence[int]) -> bool:
    if len(data) < 2:
        print('A sequence should have at least two elements!')
        return False
    for n, f_n in enumerate(data[:-2]):
        f_n1 = data[n+1]
        f_n2 = data[n+2]
        if not (f_n == f_n2 - f_n1):
            print("It's NOT a fib sequence!")
            return False
    print("It's a fib sequence!")
    return True
