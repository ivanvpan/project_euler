from math import factorial
facts = [factorial(i) for i in range(10)]
s_to_d = dict([(s, int(s)) for s in '0123456789'])
num = 11
result = 0
while True:
    s = 0
    for d in str(num):
        s = s + facts[s_to_d[d]]
    if s == num:
        result = result + num
    if num > 2999999:
        break
    num = num + 1
        
print result
