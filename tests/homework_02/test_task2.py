from homework_02.task02 import check_fib


def test_check_fib():
    assert check_fib([]) is False, 'Failed the 1st case.'
    assert check_fib([0]) is False, 'Failed the 2nd case.'
    assert check_fib([0, 1]) is True, 'Failed the 3rd case.'
    assert check_fib([0, 1, 1, 2, 3, 5, 8, 13, 21]) is True, \
                                         'Failed the 4th case.'
    assert check_fib([0, 1, 1, 2, 3, 5, 8, 13, 35]) is False, \
                                          'Failed the 5th case.'
