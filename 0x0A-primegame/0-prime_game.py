#!/usr/bin/python3
"""Module documentation"""


def isPrime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


def generatePrime(n):  # Time complexity = O(n^2)
    """Generate prime numbers in a range of number"""
    arr = []
    for i in range(n + 1):
        if isPrime(i):
            arr.append(i)
    return arr


def sieve_of_eratosthenes(n):  # Time complexity = O(n) => More efficicient
    """sieve_of_eratosthenes function"""
    arr = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if arr[p]:
            for i in range(p * p, n + 1, p):
                arr[i] = False
        p += 1
    prime = [p for p in range(2, n + 1) if arr[p]]
    return prime


def isWinner(x, nums):
    """isWinner function"""
    Maria = 0
    Ben = 0
    for i in range(x):
        arr = generatePrime(nums[i])
        if len(arr) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    else:
        return None
