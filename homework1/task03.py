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


class MinMaxStorage:
    __slots__ = ('min', 'max')

    def __init__(self):
        self.min = None
        self.max = None


def find_maximum_and_minimum(file_name: str) -> MinMaxStorage:
    values = MinMaxStorage()
    with open(file_name) as f:
        for line in f:
            curr_elem = int(line)
            if values.max is None:
                values.max, values.min = curr_elem, curr_elem
            if curr_elem > values.max:
                values.max = curr_elem
            if curr_elem < values.min:
                values.min = curr_elem
    return values.min, values.max
