# Project Euler Problem 52

# import libraries here

for i in range (1,1000000):
    x2 = sorted(str(2*i))
    x3 = sorted(str(3*i))
    x4 = sorted(str(4*i))
    x5 = sorted(str(5*i))
    x6 = sorted(str(6*i))
    if x2 == x3 and x3 == x4 and x4 == x5 and x5 == x6:
        print(i)
        break
else: print("none found")


