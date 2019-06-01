# Project Euler Problem 14

n = 0;
nMax = 0
startMax = 1
start = 0
end = 1000000
currentNum = 1

while start < end:
    start += 1
    n = 1
    currentNum = start
    while currentNum != 1:
        n += 1
        if currentNum%2 == 0:
            currentNum /= 2
        else:
            currentNum = (3*currentNum)+1
    #if start%10000 == 0:
    #    print(start, n)
    if n > nMax:
        nMax = n
        startMax = start

print(startMax, nMax)
