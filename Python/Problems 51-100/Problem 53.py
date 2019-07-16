# Project Euler Problem 53

import math

count = 0
for n in range(101):
    for r in range(n+1):
        c = math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
        if c > 1000000: count += 1
print(count)
