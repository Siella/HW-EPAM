from homework1.task04 import check_sum_of_four


def test_check_sum_of_four():
    assert check_sum_of_four([], [], [], []) == 0, 'Failed the 1st case.'
    assert check_sum_of_four([1], [2], [3], [4]) == 0, 'Failed the 2nd case.'
    assert check_sum_of_four([1], [-1], [0], [0]) == 1, 'Failed the 3rd case.'
    assert check_sum_of_four([1, 2],
                             [-1, 0],
                             [5, 23],
                             [6, -23]) == 1, 'Failed the 4th case.'
    assert check_sum_of_four([1, 2, 3],
                             [-1, 0, 3],
                             [5, 23, -3],
                             [6, -23, 3]) == 2, 'Failed the 5th case.'
