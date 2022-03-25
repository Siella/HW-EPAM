"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation
in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


# >>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator:
    fizzes = [''] * 2 + ['fizz']
    buzzes = [''] * 4 + ['buzz']
    numbers = list(map(str, range(1, n+1)))
    fizz_cnt, buzz_cnt = 0, 0
    for i, elem in enumerate(numbers):
        result = str(elem) + fizzes[i % 3] + buzzes[i % 5]
        fizz_cnt += fizzes[i % 3].count('fizz')
        buzz_cnt += buzzes[i % 5].count('buzz')
        remove_fizz = 3 * fizz_cnt
        remove_buzz = 5 * buzz_cnt
        result = result.replace(str(remove_fizz), '')
        result = result.replace(str(remove_buzz), '')
        yield result
    return


if __name__ == '__main__':
    for i in fizzbuzz(30):
        print(i)
