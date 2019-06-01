# Project Euler Problem 39

import math

p = 0
count = 0

for i in range(12,1001):
    current = 0
    for c in range(5,(i+1)//2):
        for a in range(1,c):
            b = i - c - a
            if a**2 + b**2 == c**2 and b > a: current += 1
    if current > count:
        count = current
        p = i
        print(p,count)

print(p,count)