# Project Euler Problem 26

maxCycle = 0
d = 0

for i in range(1000,1,-1):
    num = 1
    while num <= i:
        num *= 10
    remainder = 1
    count = 0
    remainders = []
    while remainder != 0:
        remainder = num%i
        if remainder in remainders:
            count = len(remainders[remainders.index(remainder):])
            break
        remainders.append(remainder)
        count += 1
        num = remainder*10
        #print(i, num, remainder, count)
    if count > maxCycle:
        maxCycle = count
        d = i
    if maxCycle > i: break
    print(i, count, d, maxCycle)

print(d, maxCycle)