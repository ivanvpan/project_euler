from itertools import product 

def multiply(data, coord, direc, depth):
    new_coord = (coord[0] + direc[0]), (coord[1] + direc[1])
    if depth == 0 \
        or new_coord[1] > len(data[0]) \
        or new_coord[0] > len(data):
        return 1
    return data[coord[0]][coord[1]] * multiply(data, new_coord, direc, depth-1)
    
data = []
for row in open('input.dat', 'r').readlines():
    data.append([int(num) for num in row.split()])
direcs = [(1, -1), (1, 0), (1, 1), (0, 1)]

maximum = 0
for i,j in product(range(20), repeat=2):
    for direc in direcs:
        maximum = max(multiply(data, (i,j), direc, 4), maximum)

print maximum
