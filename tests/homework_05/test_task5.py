from homework_05.task05 import find_maximal_subarray_sum


def test_find_maximal_subarray_sum():
    assert find_maximal_subarray_sum([], 3) is None, \
        'Failed the 1st case.'
    assert find_maximal_subarray_sum([1, 2], 0) is None, \
        'Failed the 2nd case.'
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16, \
        'Failed the 3rd case.'
    assert find_maximal_subarray_sum([1, 3, -1], 6) == 4, \
        'Failed the 4th case.'
