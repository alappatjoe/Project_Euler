# Project Euler Problem 49

# import libraries here

f = open("primes10000.txt")
primes = f.readline().split(", ")
f.close()

for i in range(len(primes)):
    primes[i] = int(primes[i])

primes = primes[primes.index(1009):]

def permutation(num1, num2):
    #print(num1, num2)
    #print(sorted(str(num1)), sorted(str(num2)))
    if sorted(str(num1)) == sorted(str(num2)): return True
    return False


for prime1 in primes:
    for prime2 in primes[primes.index(prime1)+1:]:
        prime3 = prime2 + prime2 - prime1
        if prime3 > 10000: continue
        #print(prime1, prime2, prime3)
        if prime3 in primes:
            #print("k is prime")
            if permutation(prime1,prime2) and permutation(prime1,prime3):
                print("answer:", prime1, prime2, prime3)
 
print("done")