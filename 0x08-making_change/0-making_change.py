#!/usr/bin/python3
""" Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total """
def makeChange(coins, total):
    """ make change solution using a greedy algorithm top-down
        min_coins - minimum coins needed to get total
        rem_total - Total left after each iteration
    """
    if total <= 0:
        return 0
    
    min_coins = 0
    rem_total = total

    # Sort coins in descending order
    coins.sort(reverse=True)

    for coin in coins:
        while rem_total >= coin:
            rem_total -= coin
            min_coins += 1
        
    if rem_total == 0:
        return min_coins
    else:
        return -1
