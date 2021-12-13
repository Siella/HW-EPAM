from homework5.save_original_info import custom_sum


def test_save_func_info_decorator():
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    assert 'This function can sum ' \
           'any objects which have __add___' == custom_sum.__doc__
    assert custom_sum.__name__ == 'custom_sum'
    assert callable(custom_sum.__original_func) is True
