# Project Euler Problem 3
# finding the largest prime factor of a number

import math

num = 600851475143
factors = []
primeFactors = []
prime = True

# finds 
for i in range(2, int(math.sqrt(num))):
    if num % i == 0:
        factors.append(i)

for j in factors:
    for k in range(2,int(math.sqrt(j))):
        if j % k == 0:
            prime = False
    if prime == True:
        primeFactors.append(j)

print(primeFactors[-1])
