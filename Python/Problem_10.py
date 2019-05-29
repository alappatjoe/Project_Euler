# Project Euler Problem 10

import math

num = 2000000
sum = 2
prime = True
for i in range(3,num,2):
    prime = True
    for j in range(3, int(math.sqrt(i))+1, 2):
        if i%j == 0:
            prime = False
            break
    if prime:
        sum += i

print(sum)
