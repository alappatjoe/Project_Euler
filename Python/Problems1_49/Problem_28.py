# Project Euler Problem 28

# import libraries here

sum = 1
x = 1

while x < 501:
    x += 1
    sum += 4*((2*x - 1)**2) - 12*x + 12
    print(sum, x)

print(sum)
