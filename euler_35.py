from itertools import count
from collections import deque

primes = deque()
def primegen():
    global primes
    primes = deque()
    start = 2
    for num in count(start):
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num

def rotations(num):
    n = num
    digits = 0
    while n > 0:
        n = n / 10
        digits += 1
    n = num
    n = (n / 10) + ((n % 10) * (10**(digits - 1)))
    while n != num: 
        yield n
        n = (n / 10) + ((n % 10) * (10**(digits - 1)))

def main():
    total = 0
    for prime in primegen():
        if prime > 100000:
            primes.pop()
            break

    prime_set = set(primes)
    for prime in prime_set:
        are_prime = True
        for rot in rotations(prime):
            if not rot in prime_set:
                are_prime = False
                break
        if are_prime:
            total += 1
    print total    

if __name__ == '__main__':
    main()
