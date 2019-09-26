# Project Euler Problem 4
# finding the largest palindrome made from the product of two 3-digit numbers

palin = 0
num = 0
numstr = ""


for i in range(100, 1000):
    for j in range(100, 1000):
        num = i*j
        numstr = str(num)
        if numstr[:int(len(numstr)/2)] == numstr[-1*int(len(numstr)/2):][::-1]:
            if num > palin:
                palin = num

print(palin)
