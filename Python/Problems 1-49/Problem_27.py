# Project Euler Problem 27

import Prime_Generator
import math

maxPrimes = 0
ab = 0

f = open("primes2mil.txt")
primes = f.readline()
f.close()
primes = primes[1:][:-1].split(", ")
for i in range(len(primes)):
    primes[i] = int(primes[i])

a = -999
bIndex = 0

while a < 999:
    bIndex = 0
    if int(abs(a))%100 == 99: print(a, maxPrimes, ab)
    while primes[bIndex] < 1000:
        n = 0
        primeCount = 0
        while (n*n + a*n + primes[bIndex]) in primes:
            #print(n*n + a*n + primes[bIndex])
            n += 1
            primeCount += 1
        if primeCount > maxPrimes:
            maxPrimes = primeCount
            ab = a*primes[bIndex]
        bIndex += 1
    a += 2


print(ab, maxPrimes)
