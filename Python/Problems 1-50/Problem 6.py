# Project Euler Problem 6

squaresum = 0
sumsquare = 0;
num = 100

for i in range(num+1):
    squaresum += i*i
    sumsquare += i

sumsquare *= sumsquare
print(sumsquare - squaresum)
