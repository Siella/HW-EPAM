"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: s = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
import re


def backspace_compare(first: str, second: str):
    repeat = max([first.count('#'), second.count('#')])
    first_edited, second_edited = first, second
    for _ in range(repeat):
        first_edited = re.sub(r'^#|[^#.]#', '', first_edited)
        second_edited = re.sub(r'^#|[^#.]#', '', second_edited)
    return first_edited == second_edited


if __name__ == '__main__':
    s, t = "ab#c", "ad#c"
    print(backspace_compare(s, t))
    s, t = "a##c", "#a#c"
    print(backspace_compare(s, t))
    s, t = "a#c", "b"
    print(backspace_compare(s, t))
