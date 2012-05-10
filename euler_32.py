import itertools
to9 = set('123456789')
result = set()

for perm in itertools.permutations(to9, 9):
    asstr = ''.join([str(dig) for dig in perm])
    if int(asstr[2:5]) * int(asstr[0:2]) == int(asstr[5:]) \
        or int(asstr[1:5]) * int(asstr[0]) == int(asstr[5:]):
        result.add(int(asstr[5:]))
print sum(result)
