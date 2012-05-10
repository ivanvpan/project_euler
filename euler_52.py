from itertools import count

def is_same(a, b):
    return set(str(a)) == set(str(b))

winner = 1
for i in count(1):
    prev = i
    is_the_one = True
    for mult in range(1, 7):
        if not is_same(prev, mult * i):
            is_the_one = False
            break
        prev = mult * i
    if is_the_one:
        winner = i
        break

print winner

