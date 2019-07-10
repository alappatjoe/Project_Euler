# Project Euler Problem 46

import math

f = open("primes1mil.txt")
primes = f.readline().split(", ")
f.close()

for i in range(len(primes)):
    primes[i] = int(primes[i])

num = 3

while num < primes[-1]:
    num += 2
    if num in primes: continue
    i = 1
    isSum = False
    while primes[i] + 2 <= num:
        for s in range(1,int(math.sqrt((num - primes[i])/2))+1):
            check = primes[i] + 2*(s**2)
            if num == check:
                isSum = True
                #print(num,"=", primes[i],"+ 2 *",s**2)
                break
        i += 1
        if isSum: break
    else:
        print(num)
        break
else: print("exceeded given primes")

