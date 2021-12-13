from homework2.hw4 import cache


def test_cache():
    def func_1(a, b=2):
        return (a ** b) ** 2

    def func_2(a, b=1):
        return (a ** b) ** 2

    cache_func_1 = cache(func_1)
    cache_func_2 = cache(func_2)

    some = 100, 200

    val_1 = cache_func_1(*some)
    val_2 = cache_func_1(*some)
    val_3 = cache_func_2(*some)

    assert val_1 is val_2
    assert val_1 is not val_3
