INTS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TY = ['', '', 'twen', 'thir', 'for', 'fif', 'six', 'seven', 'eigh', 'nine']
def pos_to_str(n, pos):
    if n == 0:
        return ''
    if pos == 0:
        return INTS[n]
    if pos == 1:
        return TY[n] + 'ty'
    if pos == 2:
        return INTS[n] + 'hundredand'
    if pos == 3:
        return 'onethousand'

def num_letters(num):
    total = 0
    inverse = str(num)[::-1]
    if len(inverse) > 1 and inverse[1] == '1':
        result = TEENS[int(inverse[0])]
        print result
        inverse = '00' + inverse[2:]
        total = total + len(result)
    for i, let in enumerate(inverse):
        result = pos_to_str(int(let), i)
        print result
        total = total + len(result)
    return total


def main():
    N = 1000
    total = 0
    for num in range(N+1):
        total = total + num_letters(num)
        print '-----'
    total = total - (9 * 3)
    print total

if __name__ == '__main__':
    main()

