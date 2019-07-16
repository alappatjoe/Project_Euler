# module for generating and storing primes for comparison

import Timer

primes = [2, 3]

def loadPrimes(filename):
    global primes

    f = open(filename)
    primes = f.readline().split(", ")
    f.close()
    for i in range(len(primes)):
        primes[i] = int(primes[i])

    return

def primesUpTo(upperBound):
    global primes
    #loadPrimes(upperBound)
    if primes[-1] + 1 >= upperBound: return
    ratio = ((primes[-1]+1)/upperBound)**(1/500)
    primesRecGen(upperBound, ratio)
    return

def primesRecGen(upperBound, ratio):
    global primes
    
    if ratio > 1: 
        print("ratio must be less than 1")
        return

    if primes[-1] + 1 >= upperBound:
        return

    primesRecGen(int(upperBound*ratio), ratio)
    
    #i = len(primes)
    extra = list(range(primes[-1] + 2, upperBound+1,2))
    for prime in primes[1:]:
        if prime*prime > upperBound: 
            primes.extend(extra)
            return
        k = 0
        while k < len(extra):
            if extra[k] % prime == 0: 
                extra.pop(k)
                k -= 1
            k += 1

    i = 0
    while extra[i]*extra[i] < upperBound and i < len(extra) - 1:
        j = extra.index(extra[i]*extra[i])
        while j < len(extra):
            #print(i,j)
            #print(primes)
            if extra[j]%extra[i] == 0:
                extra.pop(j)
                j -= 1
            j += 1
        i += 1
    
    primes.extend(extra)
    return

def thisManyPrimes(p):
    global primes

    num = primes[-1]
    length = len(primes)

    if length > p: return

    primes.extend([None for x in range(p-len(primes))])

    while length < p:
        num += 2
        i = 0
        while i < length and primes[i]*primes[i] <= num:
            if num%primes[i] == 0:
                break
            i += 1
        else:
            primes[length] = num
            length += 1
    
    return


def writePrimes(filename):
    f  = open(filename, "w")
    f.write(str(primes)[1:][:-1])
    f.close
    return

def isPrime(num):
    global primes

    for prime in primes:
        if prime*prime > num: break
        if num%prime == 0: return False
    return True


#Timer.startTimer()
#loadPrimes("primes100mil.txt")
#Timer.endTimer()
#Timer.printTime()
#print(len(primes))



