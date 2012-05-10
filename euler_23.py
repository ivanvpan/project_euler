import itertools, sys

def divisors_sum(n):
    divs_sum = 0
    for i in xrange(2, int(n**0.5)+1):
        if n % i == 0:
            divs_sum += i
            if i**2 != n:
                divs_sum += n / i
    return divs_sum

MAX_AB = 28123+1
all_abundant = [i for i in xrange(MAX_AB+1) if divisors_sum(i) > i]

all_num = set(xrange(MAX_AB+1))
ab =  set([(i[0] + i[1]) for i in itertools.product(all_abundant, repeat=2) if i[0] + i[1] <= MAX_AB])
result = all_num - ab
print sum(result), len(result), '+', len(ab), '=', len(all_num)
