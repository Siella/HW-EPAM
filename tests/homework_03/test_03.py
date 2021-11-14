from homework_03.hw3 import lists_combinations


def test_lists_combinations():
    assert lists_combinations([1, 2], [3, 4]) == [[1, 3],
                                                  [1, 4],
                                                  [2, 3],
                                                  [2, 4],
                                                  ], 'Fail 1'
