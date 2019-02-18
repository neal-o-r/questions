import random
import numpy as np


"""
Sample from a distribution using a BST
"""


def sample_n_bst(its, probs, n):

    out = []
    for i in range(n):
        out.append(sample_bst(its, probs))
    return np.array(out)


def sample_bst(its, probs):

    r = random.random()
    low = 0
    high = len(its)
    csum = np.cumsum(probs)

    while high >= low:
        g = (high + low) // 2
        if csum[g] < r:
            low = g + 1
        elif csum[g] - probs[g] > r:
            high = g - 1
        else:
            return its[g]


test_out = sample_n_bst(
    np.array([1, 2, 3, 4, 5]), np.array([0.1, 0.1, 0.0, 0.4, 0.4]), 10000
)


print("No. of 1's, should be ~ 1000", (test_out == 1).sum())

print("No. of 4's, should be ~ 4000", (test_out == 4).sum())

print(((test_out == 3) == 0).all())
