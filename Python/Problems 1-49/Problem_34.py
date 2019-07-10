# Project Euler Problem 34

import math

totalSum = 0



for i in range(10,999999):
    sum = 0
    for num in str(i):
        sum += math.factorial(int(num))
    if i == sum: totalSum += i

print(totalSum)
