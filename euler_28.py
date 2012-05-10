mysum = 1

def gen():
    num = 1
    diff = 2
    while True:
        for i in range(4):
            num = num + diff
            yield num
        diff = diff + 2

numgen = gen()
for side in range(3, 1002, 2):
    mysum = mysum + sum([numgen.next() for i in range(4)])

print mysum
