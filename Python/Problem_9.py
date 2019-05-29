# Project Euler Problem 9

import math

for a in range(501):
    for b in range(501):
        c = math.sqrt((a*a) + (b*b))
        if c%1 == 0 and (a+b+c) == 1000:
            print(a*b*c)