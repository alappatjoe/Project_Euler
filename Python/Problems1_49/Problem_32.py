# Project Euler Problem 32

# import libraries here

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

def digits(num):
    return len(str(num))

pandigitalNums = {1}
for i in range(1,10):
    for j in range(1000,10000):
        k = i*j
        if pandigital(int(str(i)+str(j)+str(k)),9): pandigitalNums.add(k)


for i in range(10, 100):
    for j in range(100, 1000):
        k = i*j
        if pandigital(int(str(i)+str(j)+str(k)),9): pandigitalNums.add(k)

prod = -1
for num in pandigitalNums:
    prod += num
print(pandigitalNums)
print(prod)
