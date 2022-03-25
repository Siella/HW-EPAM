"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List

import numpy as np


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = None
    while k >= 1:
        for i, elem in enumerate(nums[:-k+1]):
            curr_sum = np.sum(nums[i:i+k])
            if max_sum is None:
                max_sum = curr_sum
            if max_sum < curr_sum:
                max_sum = curr_sum
        k -= 1
    return max_sum
