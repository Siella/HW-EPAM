# I decided to write a code that generates data
# filtering object from a list of keyword parameters:
from functools import partial
from typing import Callable, List


class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list
        conforms to some criteria
    """

    def __init__(self, functions: List[Callable]):
        self.functions = functions

    def apply(self, data):
        return [
            item for item in data
            if all(i(item) for i in self.functions)
        ]


# example of usage:
# positive_even = Filter(lambda a: a % 2 == 0,
#                        lambda a: a > 0,
#                        lambda a: isinstance(int, a)))
# positive_even.apply(range(100)) should return
# only even numbers from 0 to 99


def make_filter(**keywords):
    """
        Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():
        f = partial(lambda key_, value_, dict_:
                    dict_.get(key_, '') == value_, key, value)
        filter_funcs.append(f)
    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    },
    {
        "type": "bird",
        "name": "not_polly",
    }
]

# make_filter(name='polly', type='bird').apply(sample_data)
# should return only second entry from the list

# There are multiple bugs in this code. Find them all
# and write tests for faulty cases.


if __name__ == '__main__':
    print(make_filter(name='polly', type='bird').apply(sample_data))
    positive_even = Filter([lambda a: a % 2 == 0,
                            lambda a: a > 0,
                            lambda a: isinstance(a, int)])
    print(positive_even.apply(range(100)))
