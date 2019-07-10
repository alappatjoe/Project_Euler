# Project Euler Problem 48

# import libraries here

sum = 0
mod = 10000000000

for i in range(1,1001):
    temp = 1
    for j in range(i):
        temp *= i
        temp %= mod
    sum += temp
    sum %= mod

print(sum)
