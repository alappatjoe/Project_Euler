# Project Euler Problem 2

sum = 0
fib1 = 1
fib2 = 1

while fib2 <= 4000000:
    fib2 = fib1 + fib2
    if fib2%2 == 0:
        sum += fib2
    fib1 = fib2 - fib1

print(sum)