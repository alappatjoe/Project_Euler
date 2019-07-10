# Prime Generation module
# returns list 'primes' with desired prime numbers


def primesUpTo(upperBound):

    primes = list(range(3,upperBound+1,2))
    primes.insert(0,2)
    i = 1

    while i < len(primes) - 1 and primes[i]*primes[i] < upperBound:
        j = primes.index(primes[i]*primes[i])
        while j < len(primes):
            #print(i,j)
            #print(primes)
            if primes[j]%primes[i] == 0:
                primes.pop(j)
                j -= 1
            j += 1
        i += 1
    f  = open("primes1mil.txt", "w")
    f.write(str(primes))
    f.close
    return primes

def thisManyPrimes(p):

    num = 1
    primes = [None for x in range(p)]
    primes[0] = 2
    length = 1

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
    
    return primes
