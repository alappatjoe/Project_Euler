# Project Euler Problem 58

import math

def primeCheck(num):
    if num <= 2: return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0: return False

    return True

s = 3
ratio = 1
primeCount = 0
while ratio >= .1:
    bl = (s**2) - s + 1
    tl = bl - s + 1
    tr = tl - s + 1
    #print(s, primeCount, bl, tl, tr)
    if primeCheck(bl): primeCount += 1
    if primeCheck(tl): primeCount += 1
    if primeCheck(tr): primeCount += 1
    ratio = primeCount / (2*s - 1)
    s += 2

print(s-2, ratio)


    
