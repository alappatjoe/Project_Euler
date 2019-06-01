# Project Euler Problem 30

# import libraries here

totalSum = 0
nums = []
max = 354295

for i in range(2,max):
    sum = 0
    num = i
    while num > 0:
        sum += (num%10)**5
        num //= 10
    if sum == i:
        nums.append(i)
        totalSum += i

print(nums)
print(totalSum)
