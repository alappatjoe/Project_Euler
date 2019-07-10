# Project Euler Problem 5

num = 1
i = 0
gcf = 1
for i in range(1,21):
    gcf = 1
    for j in range(1,i+1):
        if num%j==i%j==0:
            gcf = j
    num *= i/gcf

print(num)
