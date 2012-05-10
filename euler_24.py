from math import factorial
NUMS = [0,1,2,3,4,5,6,7,8,9]

def perm(TARGET):
    nums = [i for i in NUMS]
    temp = TARGET
    result = []
    for i in range(len(nums)-1, 0, -1):
        multi = temp/factorial(i)
        result.append(multi)
        temp = temp - (factorial(i) * multi)
        if temp == 0:
            break

    for i in result:
        print nums[i],
        del nums[i]
    for i in nums:
        print i,

perm(999999)
