from itertools import count

def primes_to(n):
    primes = []
    for i in count(2):
        if i > n:
            break
        is_prime = True
        for prim in primes:
            if i % prim == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

#PRIMES = primes_to(10000)

def prime_factors(n):
    upto = n/2
    divisors = []
    for i in PRIMES:
        if i > upto:
            break
        if n % i == 0:
            divisors.append(i)
    return divisors

DIV_SUM = {}

def divisors(n):
    divs = set()
    div_sum = 0
    upto = n**0.5
    for i in xrange(1, n+1):
        if n % i == 0:
            divs.add(i)
            div_sum = div_sum + i
        if i > upto:
            break
    if 1 in divs:
        divs.remove(1)
    for div in divs:
        div_sum = div_sum + n/div
    return div_sum

def is_amicable(n):
    if DIV_SUM.has_key(n):
        div_sum = DIV_SUM[n]
    else:
        div_sum = (divisors(n))
        DIV_SUM[n] = div_sum
    
    if DIV_SUM.has_key(div_sum):
        snd_sum = DIV_SUM[div_sum]
    else:
        snd_sum = (divisors(div_sum))
        DIV_SUM[div_sum] = snd_sum

    return (n == snd_sum) and (n != div_sum)

def main():
    N = 10000
    amic = []
    for i in xrange(0,N+1):
        if is_amicable(i):
            amic.append(i)
    print sum(amic)
    #print len(DIV_SUM)


if __name__ == '__main__':
    main()
