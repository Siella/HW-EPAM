from homework_02.hw2 import major_and_minor_elem


def test_major_and_minor_elem():
    assert major_and_minor_elem([1, 2], [3, 4]) == (3, 2), 'Fail 1'
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1), 'Fail 2'
    assert major_and_minor_elem([2, 3, 1, 1, 1, 2]) == (1, 3), 'Fail 3'
