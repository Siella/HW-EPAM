"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import itertools
from typing import List

import numpy as np


def check_sum_of_four(a: List[int],
                      b: List[int],
                      c: List[int],
                      d: List[int]) -> int:
    K, N = 4, len(a)
    matrix = np.array([a, b, c, d])
    cnt_tuples = 0
    for i in itertools.product([0, 1], repeat=K * N):
        ones_matrix = np.reshape(np.array(i), (N, K))
        if all(ones_matrix.sum(axis=0) == np.array([1, 1, 1, 1])):
            if np.matmul(matrix, ones_matrix).trace() == 0:
                cnt_tuples += 1
    return cnt_tuples
