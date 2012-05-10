def sum_digits(num):
    return sum([int(i) for i in str(num)])

max_sum = 0
for a in range(101):
    for b in range(101):
        new_sum = sum_digits(a**b)
        if new_sum > max_sum:
            max_sum = new_sum

print max_sum
