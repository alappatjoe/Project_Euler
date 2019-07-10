# Project Euler Problem 37

# import libraries here

f = open("primes1mil.txt")
primes = f.readline().split(", ")
f.close()

truncatable = []
sum = 0

for prime in primes:
    if len(prime) == 1: continue
    for i in range(1,len(prime)):
        left = prime[i:]
        right = prime[:i]
        if left in primes and right in primes: continue
        else: break
    else: 
        truncatable.append(prime)
        sum += int(prime)
        print(prime)
    if len(truncatable) >= 11: break

print(truncatable)
print(sum)
