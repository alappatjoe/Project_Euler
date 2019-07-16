# Project Euler Problem 57

# import libraries here

n = 1
d = 1
count = 0
for i in range(1000):
    n += d * 2
    d = n - d
    if len(str(n)) > len(str(d)): count += 1

print(count)