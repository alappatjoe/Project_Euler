# Project Euler Problem 56

# import libraries here

def digitSum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

maxDigitSum = 0
num = 0
numa = 0
numb = 0
for a in range(2,100):
    if a%10 == 0: continue
    for b in range(1,100):
        ab = a**b
        digits = digitSum(ab)
        if digits > maxDigitSum:
            maxDigitSum = digits
            num = ab
            numa = a
            numb = b

print(maxDigitSum, a, b, ab)

