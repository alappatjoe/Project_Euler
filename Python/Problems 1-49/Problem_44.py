# Project Euler Problem 44

import math

def pentagonal(num):
    n = (math.sqrt(24*num + 1) + 1)/6
    return n == int(n)

k = 0
done = False

while not done:
    k += 1
    pk = k*(3*k - 1)/2
    if not pentagonal(pk): continue
    for j in range(k-1,0,-1):
        pj = j*(3*j - 1)/2
        if not pentagonal(pj): continue
        if pentagonal(pk - pj) and pentagonal(pj + pk):
            done = True
            print("j =",j,"\t k =",k)
            print("D =", pk - pj)
            break

