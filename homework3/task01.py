from typing import Callable


def cache(times: int) -> Callable:
    def wrapped_cache(func: Callable) -> Callable:
        cache_dict = dict()

        def access_cache(*args, **kwargs):
            key = str((args, kwargs))
            if key not in cache_dict:
                cache_dict[key] = (func(*args, **kwargs), -1)
            func_val, func_times = cache_dict[key]
            if func_times == times:
                del cache_dict[key]
                return func(*args, **kwargs)
            else:
                cache_dict[key] = (func_val, func_times + 1)
                return func_val
        return access_cache
    return wrapped_cache


@cache(times=2)
def f(some_kwarg=0):
    return input('? ')
