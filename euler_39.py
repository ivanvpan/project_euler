#!/usr/bin/python
def is_triangle(a, b, c):
    return (c < (a + b) and \
            a < (b + c) and \
            b < (a + c))

def is_square(a, b, c):
    return a**2 + b**2 == c**2

max_pair = (0, 0)
for PERIM in xrange(1000):
    results = []
    for a in xrange(PERIM/4, PERIM/2):
        for b in xrange(a):
            c = PERIM - a - b
            if c > a:
                continue
            if is_square(c,b,a):
                results.append((a,b,c))
    if len(results) > max_pair[0]:
        max_pair = (len(results), PERIM)
        print max_pair

print max_pair
