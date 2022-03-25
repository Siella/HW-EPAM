from homework7.hw2 import backspace_compare


def test_backspace_compare():
    assert backspace_compare("ab#c", "ad#c") is True
    assert backspace_compare("a##c", "#a#c") is True
    assert backspace_compare("a#c", "b") is False
    assert backspace_compare("###a", "a") is True
    assert backspace_compare("ab###", "") is True
    assert backspace_compare("ab###", "###") is True
