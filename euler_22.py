names = [name.strip('"') for name in open('names.txt').read().split(',')]
names.sort()

total = 0
for i, name in enumerate(names):
    word_value = sum([(ord(let) - 64) for let in name])
    total = total + word_value * (i + 1)
print total
