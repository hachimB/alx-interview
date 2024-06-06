#!/usr/bin/python3
"""Module documentation"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], 1 + dp[amount - coin])
    return -1 if dp[total] == float('inf') else dp[total]
