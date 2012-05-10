from operator import mul
from math import factorial

COINS = [1, 2, 5, 10, 20, 50, 100, 200]
COINS.reverse()

def break_max(value):
    coins = []
    temp_val = value
    i = 0
    while sum(coins) < value and i < len(COINS):
        if COINS[i] == value:
            i = i + 1
            continue
        temp_val = temp_val - COINS[i]
        if temp_val >= 0:
            coins.append(COINS[i])
        else:
            temp_val = temp_val + COINS[i]
            i = i + 1
    # print value, '=>', ','.join([str(c) for c in coins])
    return coins

def multiset(n, k):
    if n < k:
        return 1
    a = 1
    i = n + k - 1
    while i >= k:
        a = a * i
        i = i - 1

    b = 1
    i = 1
    while i <= n-k:
        b = b * i
        i = i + 1
    #return a/b
    return factorial(n + k - 1)/(factorial(k) * factorial(n - k))

def ways(value):
    if value == 1:
        return 1
    coins = break_max(value)
    coin_set = set(coins)
    result = 1
    for coin in coin_set:
        result = result * multiset(ways(coin), coins.count(coin))
    if value in COINS:
        result = result + 1
    print value, '=>', result
    return result

