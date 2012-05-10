powers = []
power = 0
while True:
    res = 2**power
    if res > 1000000:
        break
    powers.append(2**power)
    power += 1
powers.reverse()
    
def is_palin(s):
    palindrome = True
    for i, l in enumerate(s):
        if l != s[len(s)-1-i]:
            palindrome = False
    return palindrome

def to_binary_str(n):
    rem = n
    digits = []
    for i in powers:
        if i > n:
            continue
        if rem - i >= 0:
            digits.append('1')
            rem = rem - i
        else:
            digits.append('0')
    return ''.join(digits)

def main():
    total = 0
    for i in xrange(1000000):
        if is_palin(str(i)) and is_palin(to_binary_str(i)):
            total += i
    print total

if __name__ == '__main__':
    main()
