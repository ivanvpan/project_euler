from itertools import count

primes = []
def primegen():
    if not primes:
        start = 2
    else:
        start = primes[-1]
    for num in count(start):
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num

def prime_factors(n):
    result = []
    root = n**0.5
    pgen = primegen()
    if not primes:
        pgen.next()
    while primes[-1] < root:
        pgen.next()
    for prime in primes:
        if n % prime == 0:
            result.append(prime)
    return result

def factorization(n):
    factors = prime_factors(n)
    result = []
    for fac in factors:
        power = 0
        div = n
        while div % fac == 0:
            div = div / fac
            power = power + 1
        result.append((fac, power))
    return result
 
def total_divisors(n):
    factors = factorization(n)
    divs = 1
    for fac in factors:
        divs = divs * (fac[1] + 1)
    if divs == 0:
        divs = 2
    return divs

def trigen():
    sum_ = 0
    for i in count(1):
        sum_ = sum_ + i
        yield sum_

def main():
    for tri in trigen():
        divs = total_divisors(tri)
        if divs > 500:
            print tri
            break

if __name__ == '__main__':
    main()
