import time

from task02.task02 import parallel_slow_calculate


def test_parallel_slow_calculate():
    start_time = time.time()
    parallel_slow_calculate(30, range(500))
    assert time.time() - start_time < 60, \
        'Too slow! Try increase num of pools'
