"""
Write down the function, which reads input line-by-line, and find maximum and
minimum values. Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""


class MinMaxTuple:
    __slots__ = ('min', 'max')

    def __init__(self):
        self.min = -1
        self.max = -1


def find_maximum_and_minimum(file_name: str) -> MinMaxTuple:
    first = True
    values = MinMaxTuple()
    with open(file_name) as f:
        for line in f:
            curr_elem = int(line)
            if first:
                values.max = curr_elem
                values.min = curr_elem
                first = False
                continue
            if curr_elem > values.max:
                values.max = curr_elem
            if curr_elem < values.min:
                values.min = curr_elem
        if first:
            print('An empty file!')
            return values.min, values.max
    return values.min, values.max
