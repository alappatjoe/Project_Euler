# Project Euler Problem 41

import math


def pandigital(num, n):
    numstr = str(num)
    if len(numstr) != n: return False
    nums = set(range(1,n+1))
    for char in numstr:
        try:
            nums.remove(int(char))
        except:
            return False
    return True

def isPrime(num):
    if num%2 == 0: return False
    for i in range(3,int(math.sqrt(num))+1,2):
        if num%i == 0: return False
    return True

num = 7654321
panNums = []
while num >= 1234567:
    if pandigital(num,7): panNums.append(num)
    num -= 1

num = 4321
while num >= 1234:
    if pandigital(num,4): panNums.append(num)
    num -= 1

for val in panNums:
    if isPrime(val):
        print(val)


