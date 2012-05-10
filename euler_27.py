from itertools import count
from collections import deque

N = 1000

def primes(n):
    sieve = set(xrange(3, n+1, 2))
    for i in xrange(3, n+1, 2):
        if i in sieve:
            prod = 1
            mult = 2
            while prod < n:
                prod = i * mult
                mult += 1
                if prod not in sieve:
                    continue
                sieve.remove(prod)
    return sieve

MAX_NUM = 78**2 + 78*N + N
PRIMES = primes(MAX_NUM)

def count_primes(a,b):
    total = 0
    for n in count(0):
        result = plug(n, a, b)
        if result in PRIMES:
            total += 1
        else:
            break
    return total
        
def plug(n, a, b):
    return n * n + a * n + b

max_tuple = (0, 0, 0)
for a in range(-N, N+1):
    for b in range(-N, N+1):
        num_primes = count_primes(a, b)
        if num_primes > max_tuple[0]:
            max_tuple = (num_primes, a, b)

print max_tuple
print max_tuple[1] * max_tuple[2]
