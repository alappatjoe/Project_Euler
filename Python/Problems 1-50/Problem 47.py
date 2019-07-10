# Project Euler Problem 47

import math

f = open("primes1mil.txt")
primes = f.readline().split(", ")
f.close()

for i in range(len(primes)):
    primes[i] = int(primes[i])

def numPrimeFactors(num):
    pfactors = {1}
    i = 0
    x = num
    while primes[i] <= x:
        if x%primes[i] == 0: 
            x /= primes[i]
            pfactors.add(primes[i])
            i -= 1
        i += 1
    pfactors.remove(1)
    return len(pfactors)

num = 210
consecutive = 0

while consecutive < 4:
    numFactors = numPrimeFactors(num)
    if numFactors >= 4: consecutive += 1
    else: consecutive = 0
    #if num%10000 == 0: print(num, numFactors, consecutive)
    num += 1

num -= 1
print(num-3,num-2,num-1,num)
