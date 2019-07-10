# Project Euler Problem 50

# import libraries here

f = open("primes1mil.txt")
primes = f.readline().split(", ")
f.close()

primes[0] = 2
primeSum = [0, 2]

for i in range(1,len(primes)):
    primes[i] = int(primes[i])
    primeSum.append(primes[i] + primeSum[i])
    

maxRange = 1
maxRangePrime = 2
for i in range(len(primes)):
    for j in range(i-maxRange,-1,-1):
        k = i - j
        num = primeSum[i] - primeSum[j]
        #print(i,j,k,primes[i],primeSum[i+1], primes[j],primeSum[j+1], num)
        if num > 1000000:
            break
        if num in primes and k > maxRange:
                maxRange = k
                maxRangePrime = num
                print(i, j, k, num)



print(maxRange, maxRangePrime)
