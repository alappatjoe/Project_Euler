# Project Euler Problem 51

import math

def primeCheck(num):
    if num <= 2: return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0: return False

    return True

patterns = [["0","0","0","1","2","3"],
            ["0","0","1","0","2","3"],
            ["0","0","1","2","0","3"],
            ["0","1","0","0","2","3"],
            ["0","1","0","2","0","3"],
            ["0","1","2","0","0","3"],
            ["1","0","0","0","2","3"],
            ["1","0","0","2","0","3"],
            ["1","0","2","0","0","3"],
            ["1","2","0","0","0","3"]]


for i in range(1,1000,2):
    #print(i)
    if i % 5 == 0 or i % 3 == 0: continue
    d3 = i % 10
    d2 = (i // 10) % 10
    d1 = (i // 100) % 10
    d = [d1,d2,d3]
    #print(d)
    for j in range(10):
        notPrime = 0
        primes = []
        for k in range(10):
            #print(i,j,k)
            pattern = list(patterns[j])
            #print(pattern)
            
            for m in range(1,4):
                pattern[pattern.index("0")] = k
                pattern[pattern.index(str(m))] = d[m-1]
            num = 0
            for val in pattern:
                num = (num * 10) + val
            #print(num)
            if not primeCheck(num): 
                notPrime += 1
                if notPrime > 2: break
            else: 
                primes.append(num)
                #print(primes)
        else: print(primes)







