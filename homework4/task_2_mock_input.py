"""
Write a function that accepts an URL as input
and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - test could be run without internet connection

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


# >>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
import urllib.request


class AnotherExceptions(Exception):
    pass


def count_dots_on_i(url: str) -> int:
    try:
        with urllib.request.urlopen(url) as f:
            html = f.read().decode('utf-8')
            return html.count('i')
    except ConnectionError:
        raise ValueError(f"Unreachable {url}")
    except Exception as ex:
        raise AnotherExceptions(f"{type(ex).__name__}, {ex.args}")


if __name__ == '__main__':
    print(count_dots_on_i("https://example.com/"))
