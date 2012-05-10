result = []

def check(x, y):
    if not x in result or not y in result:
        if not x in result:
            result.append(x)
        if not y in result:
            result.append(y)
    else:
       ix = result.index(x)
       iy = result.index(y)
       if ix > iy:
           result.remove(y)
           result.insert(ix, y)
    
f = open('keylog.txt')
lines = [l.strip() for l in f.readlines()]
for l in lines:
    check(l[0], l[1])
    check(l[1], l[2])

print result

