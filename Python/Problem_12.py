# Project Euler Problem 12

import math
index = 0
triangle = 1
divisors = 0
while divisors <= 500:
    index += 1
    triangle = int(index*(index+1)/2)
    divisors = 0
    sqroot = math.sqrt(triangle)
    for j in range(1, int(sqroot)):
        if triangle%j == 0:
            divisors += 2
    if int(sqroot)*int(sqroot) == triangle:
        divisors -= 1
print(triangle, divisors)