from task03.task03 import Filter, make_filter, sample_data


def test_positive_even_numbers():
    positive_even = Filter([lambda a: a % 2 == 0,
                            lambda a: a > 0,
                            lambda a: isinstance(a, int)])
    assert positive_even.apply(range(100)) == list(range(100)[2::2])


def test_make_filter():
    assert make_filter(name='polly',
                       type='bird').apply(sample_data) == [sample_data[1]]
