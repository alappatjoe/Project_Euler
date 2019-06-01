# Project Euler Problem 7


import math

num = 10001

isPrime = True
primes = [2]
i = 1
while len(primes) < num:
    i += 2
    isPrime = True
    for p in primes:
        if i%p == 0:
            isPrime = False
    if isPrime:
        primes.append(i)
        print(len(primes), i)

print(primes[-1])
