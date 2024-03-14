#!/usr/bin/python3
"""
0-prime_game
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count primes in the range
        primes = [i for i in range(2, n+1) if is_prime(i)]
        
        # Determine the winner based on the number of primes
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None