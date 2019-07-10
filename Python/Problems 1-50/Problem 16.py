# Project Euler Problem 16

num = [1]
pow = 1000
val = 0
carry = 0
for i in range(pow):
    carry = 0
    for j in range(len(num)):
        val = 2*num[j] + carry
        carry = int(val/10)
        num[j] = val%10
        if j == len(num)-1:
            num.append(carry)


sum = 0
for vals in num:
    sum += vals
print(sum)
