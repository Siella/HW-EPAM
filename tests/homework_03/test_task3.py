import os

from homework_03.task03 import find_maximum_and_minimum


def test_find_maximum_and_minimum():
    def find(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
    test_file1 = find('test1.txt', os.getcwd())
    test_file2 = find('test2.txt', os.getcwd())
    test_file3 = find('test3.txt', os.getcwd())
    assert find_maximum_and_minimum(test_file1) == (-1, -1), \
        'Failed the 1st case.'
    assert find_maximum_and_minimum(test_file2) == (1, 1), \
        'Failed the 2nd case.'
    assert find_maximum_and_minimum(test_file3) == (1, 5), \
        'Failed the 3rd case.'
