# Project Euler Problem 23

import math

def divisors(x):
    returnSet = {1}
    for i in range(1,int(math.sqrt(x))+1):
        if x%i == 0:
            returnSet.add(i)
            returnSet.add(x/i)
    returnSet.remove(x)
    return returnSet


def perfection(x):
    checkSum = 0
    for factor in divisors(x):
        checkSum += factor
    if checkSum > x:
        return "abundant"
    elif checkSum < x:
        return "deficient"
    else:
        return "perfect"

abundant = []
answerSet = {1}
for num in range(1,28123):
    if perfection(num) == "abundant":
        abundant.append(num)
        for i in range(len(abundant)):
            if num + abundant[i] < 28123:
                answerSet.add(num + abundant[i])
answerSet.remove(1)

nums = set(range(28123))
sum = 0
for number in answerSet:
    if number in nums: nums.remove(number)

for num in nums:
    sum+=num

print(nums, sum)
