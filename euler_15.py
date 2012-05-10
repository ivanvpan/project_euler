N = 20

def sum_middle(row):
    result = []
    for i in range(len(row)-1):
        a = row[i]
        b = row[i+1]
        result.append(a+b)
    return result

row = [1]
for i in range(N):
    row = sum_middle([0]+row+[0])
for i in range(N):
    row = sum_middle(row)

print row
    
        
