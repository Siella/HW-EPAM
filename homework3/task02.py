import hashlib
import random
import struct
import time
from multiprocessing import Pool
from typing import List


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def parallel_slow_calculate(num_pools: int,
                            value_list: List) -> int:
    p = Pool(num_pools)
    with p:
        result = p.map(slow_calculate, value_list)
    return sum(result)


if __name__ == '__main__':
    start_time = time.time()
    slow_calculate(1)
    print("--- %s seconds per call ---" % (time.time() - start_time))

    start_time = time.time()
    parallel_slow_calculate(30, range(500))
    print("--- %s seconds ---" % (time.time() - start_time))
