# Project Euler Problem 21

import math

nums = {0}
max = 10000
totalSum = 0

def d(x):
    sum = 0
    for i in range(1,int(math.sqrt(x))):
        if x%i == 0:
            if i == 1 or i*i == x: sum += i
            else: sum += i + x/i
    return sum

for x in range(1,max):
    b = d(x)
    a = d(b)
    if x == a and a != b:
        nums.add(a)
        nums.add(b)

for num in nums:
    totalSum += num

print(totalSum)
