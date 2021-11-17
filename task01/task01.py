from typing import Callable

cache_dict = dict()


def cache(times: int) -> Callable:
    def wrapped_cache(func: Callable) -> Callable:
        global cache_dict

        def access_cache(*args):
            if args not in cache_dict:
                cache_dict[args] = (func(*args), -1)
            func_val, func_times = cache_dict[args]
            if func_times == times:
                del cache_dict[args]
                return func(*args)
            else:
                cache_dict[args] = (func_val, func_times + 1)
                return func_val
        return access_cache
    return wrapped_cache


@cache(times=2)
def f():
    return input('? ')
