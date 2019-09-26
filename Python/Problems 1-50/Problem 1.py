# Project Euler Problem 1
# sum of all multiples of 3 and 5 below 1000

sum = 0

for num in range(1000):
    if num%3 == 0 or num%5 == 0:
        sum += num
   
print(sum)
