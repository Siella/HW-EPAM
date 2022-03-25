from homework3.task01 import cache


def test_cache():

    invoked = 0

    @cache(times=3)
    def func_1(a, b=2):
        return (a ** b) ** 2

    @cache(times=2)
    def func_2(a, b=1):
        nonlocal invoked
        invoked += 1
        return a + b

    some = 100, 200

    assert invoked == 0

    val_1 = func_1(*some)
    val_2 = func_1(*some)
    for i in range(8):
        val_3 = func_2(*some)

    assert val_1 is val_2
    assert val_1 is not val_3
    assert invoked == 4
