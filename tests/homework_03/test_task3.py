import os

from homework_03.task03 import find_maximum_and_minimum


def test_find_maximum_and_minimum():
    PATH = os.getcwd()
    assert find_maximum_and_minimum(PATH+'/test1.txt') == (-1, -1), \
        'Failed the 1st case.'
    assert find_maximum_and_minimum(PATH+'/test2.txt') == (1, 1), \
        'Failed the 2nd case.'
    assert find_maximum_and_minimum(PATH+'/test3.txt') == (1, 5), \
        'Failed the 3rd case.'
