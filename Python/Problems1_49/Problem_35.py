# Project Euler Problem 35

# import libraries here

f = open("primes1mil.txt")
primes = f.readline().split(", ")
f.close()

circprimes = []

for numstr in primes:
    if "2" in numstr or "4" in numstr or "6" in numstr: continue
    if "8" in numstr or "0" in numstr or "5" in numstr: continue
    for i in range(1,len(numstr)):
        newNum = numstr[i:]+numstr[:i]
        if newNum in primes: continue
        else: break
    else: 
        circprimes.append(numstr)

circprimes.insert(0, "2")
circprimes.insert(2, "5")

print(circprimes)
print(len(circprimes))

