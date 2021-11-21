"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
import math
from typing import Sequence


def binet_formula(n: int):
    phi = (1 + math.sqrt(5)) / 2
    return int((phi ** n - (1 - phi) ** n) / (2 * phi - 1))


def fib_seq_generator(n: int):
    while True:
        yield binet_formula(n)
        n += 1
    return


def check_fib(data: Sequence[int]) -> bool:
    """
    Checks whether data is a Fibonacci SUBsequence.
    """
    first_element = data[0]
    for n, f_n in enumerate(fib_seq_generator(0)):
        if first_element == f_n:
            break
        if n >= len(data):
            print("It's NOT a fib sequence!")
            return False
    for our_elem, true_elem in zip(data, fib_seq_generator(n)):
        if our_elem != true_elem:
            print("It's NOT a fib sequence!")
            return False
    print("It's a fib sequence!")
    return True
