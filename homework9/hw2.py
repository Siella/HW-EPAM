"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

# >>> with supressor(IndexError):
# ...    [][2]

"""
import contextlib


class SuppressorClass:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type != self.exception:
            raise exc_type
        pass
        return True


@contextlib.contextmanager
def context_manager_suppressor(exception):
    try:
        yield
    except exception:
        pass


if __name__ == '__main__':
    with SuppressorClass(IndexError):
        [][2]

    with context_manager_suppressor(IndexError):
        [][2]
