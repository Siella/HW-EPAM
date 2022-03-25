"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    uniq_vals = set(inp)
    cnt_occur = {val: inp.count(val) / 2 for val in uniq_vals}
    common_elements = dict(filter(lambda x: x[1] >= 1, cnt_occur.items()))
    most_common = max(common_elements, key=common_elements.get)
    least_common = min(cnt_occur, key=cnt_occur.get)
    return most_common, least_common
