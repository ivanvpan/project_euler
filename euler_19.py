M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 1901
day = 1
month = 0
total = 0
leap = 0

while not (year == 1902 and month == 0):
    print year, month, day
    if day % 7 == 0:
        total = total + 1

    if month == 1 and year % 4 == 0:
        leap = leap + 1
        day = day + 29
    else:
        day = day + M[month]

    if month == 11:
        month = 0
        year = year + 1
    else:
        month = month + 1
 
print total


