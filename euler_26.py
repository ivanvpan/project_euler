def power_of_10(d):
    power = 1
    while d > 10**power:
        power += 1
    return power

def max_length(d):
    power = power_of_10(d)
    initial = 10**power
    tried = set()
    counter = 0
    while True:
        tried.add(initial)
        counter += 1
        initial = (initial % d) * (10**power)
        if initial in tried or initial == 0:
            return counter

max_d = (0,0)
for d in range(1,1001):
    max_l = max_length(d)
    if max_l > max_d[1]:
        max_d = (d, max_l)

print max_l
