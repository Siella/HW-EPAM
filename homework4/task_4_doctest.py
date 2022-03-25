"""
Write a function that takes a number N as an input
and returns N FizzBuzz numbers*.
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15,
"Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    >>> fizzbuzz(0)
    []
    >>> fizzbuzz(3)
    ['1', '2', 'fizz']
    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(6)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz']
    >>> output = ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7',\
    '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    >>> fizzbuzz(15) == output
    True
    >>> fizzbuzz(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    """
    if n < 0:
        raise ValueError('n must be >= 0')
    fb_list = list(map(str, range(1, n+1)))
    for fizz_idx in range(2, n, 3):
        fb_list[fizz_idx] = 'fizz'
    for buzz_idx in range(4, n, 5):
        if fb_list[buzz_idx] == 'fizz':
            fb_list[buzz_idx] = 'fizzbuzz'
        else:
            fb_list[buzz_idx] = 'buzz'
    return fb_list


if __name__ == '__main__':
    import doctest
    doctest.testmod()
