import os

from homework1.task03 import find_maximum_and_minimum


def test_find_maximum_and_minimum():
    def find_tests(name):
        return os.path.join(os.path.dirname(__file__), name)
    test_file1 = find_tests('test1.txt')
    test_file2 = find_tests('test2.txt')
    test_file3 = find_tests('test3.txt')
    assert find_maximum_and_minimum(test_file1) == (None, None), \
        'Failed the 1st case.'
    assert find_maximum_and_minimum(test_file2) == (1, 1), \
        'Failed the 2nd case.'
    assert find_maximum_and_minimum(test_file3) == (1, 5), \
        'Failed the 3rd case.'
