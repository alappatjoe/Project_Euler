# Project Euler Problem 36

# import libraries here

doublepalin = []
sum = 0

for i in range(1000000):
    numstr = str(i)
    binNum = bin(i)[2:]
    if numstr == numstr[-1::-1] and binNum == binNum[-1::-1]:
        doublepalin.append(i)
        sum += i

print(doublepalin)
print(sum)