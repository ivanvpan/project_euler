import operator

def by_frequency(alist):
    table = {}
    for item in alist:
        if item not in table:
            table[item] = 1
        else:
            table[item] = table[item] + 1
    return [tup[0] for tup in sorted(table.items(), key=operator.itemgetter(1), reverse=True)]


f = open('cipher1.txt')
text = f.read().split(',')
text_list = list(text)

letters = 'e t a o i n s r h l d c u m f p g w y b v k x j q z'
let_list = letters.split()

per_key = []
for j in range(3):
    chars = by_frequency([text[i] for i in range(j, len(text), 3)])
    per_key.append(chars)

for i in range(3):
    print ' '.join(per_key[i]), len(per_key[i])
#    for ch in range(i, len(text_list), 3):
#        print


