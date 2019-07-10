# Project Euler Problem 25

fib1 = 1
fib2 = 1
index = 2

while len(str(fib2)) < 1000:
    index += 1
    fib2 = fib1 + fib2
    fib1 = fib2 - fib1

print(index, fib2)


