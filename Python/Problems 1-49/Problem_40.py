# Project Euler Problem #

# import libraries here

num = ""
i = 0

while len(num) < 1000000:
    i += 1
    num += str(i)

val = int(num[0])*int(num[9])*int(num[99])*int(num[999])*int(num[9999])*int(num[99999])*int(num[999999])
print(val)