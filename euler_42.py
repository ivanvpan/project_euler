words = [w.strip('"') for w in open('words.txt').read().split(',')]
roots = lambda n: (-1 + (1 + 8 * n)**0.5) / 2
total = 0
for w in words:
    root = roots(reduce(lambda x,y: x + ord(y) - 64, w, 0))
    if int(root) == root:
        total += 1
print total
