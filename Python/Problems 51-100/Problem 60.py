# Project Euler Problem 60

import Timer, Primes, math

def concat(x, y):

    a = math.floor(math.log10(y))
    return int(x*10**(1+a)+y)



    #num = int(str(x)+str(y))
    #return num

def splitPrimes(primeInput):
    primeMod = [[3],[3]]
    for prime in primeInput[2:]:
        primeMod[(prime%3) - 1].append(prime)
    return primeMod

def primeSet(primes, n):
    #print(primes, n)
    if n < 1: 
        print("n must be greater than 1")
        return
    if n == 1:
        returnSet = [[primes[i]] for i in range(len(primes))]
        return returnSet
    else:
        print(n, "start")
        returnSet = []
        pSets = primeSet(primes, n-1)
        Timer.startTimer()
        for i in range(len(pSets)):
            for j in range(i,len(pSets)):
                if pSets[i][1:] == pSets[j][:-1]:
                    if Primes.isPrime(concat(pSets[i][0],pSets[j][-1])) and Primes.isPrime(concat(pSets[j][-1], pSets[i][0])):
                        temp = list(pSets[i])
                        temp.append(pSets[j][-1])
                        returnSet.append(temp)
        Timer.endTimer()
        Timer.printTime()
        print("Sets of", n, ":", len(returnSet))
        return returnSet
    return

Primes.loadPrimes("primes10000.txt")
checkedPrimes = list(Primes.primes)
#Primes.loadPrimes("primes1mil.txt")

split = splitPrimes(checkedPrimes)
sets = primeSet(split[0],5)
sets.extend(primeSet(split[1],5))
for set in sets:
    print(set, sum(set))




