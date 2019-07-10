# Project Euler Problem 45

import math

def pentagonal(num):
    n = (math.sqrt(24*num + 1) + 1)/6
    return n == int(n)

def hexagonal(num):
    n = (math.sqrt(8*num + 1) + 1)/4
    return n == int(n)

answers = []
triIndex = []
pentIndex = []
hexIndex = []
n = 0
while len(answers) < 3:
    n += 1
    t = n*(n+1)/2
    if pentagonal(t) and hexagonal(t):
        answers.append(t)
        triIndex.append(n)
        pentIndex.append((math.sqrt(24*t + 1) + 1)/6)
        hexIndex.append((math.sqrt(8*t + 1) + 1)/4)

print(answers)
print(triIndex)
print(pentIndex)
print(hexIndex)