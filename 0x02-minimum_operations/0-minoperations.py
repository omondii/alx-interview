#!/usr/bin/python3
""" Total no. of ops required to copy items from a file """
import sys


def minOperations(n: int) -> int:
    """ func minOperations returns the total number of
    times needed to complete an action n times
    dp: list with each element set to the maximum representable integer value
    """
    dp = [sys.maxsize] * (n + 1)
    # Initial state
    dp[1] = 0
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[i]
