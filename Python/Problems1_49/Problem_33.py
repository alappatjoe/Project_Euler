# Project Euler Problem 33

# import libraries here

numer = []
denom = []



for i in range(11,99):
    for j in range(i+1,100):
        istr = str(i)
        jstr = str(j)
        if istr[0] == jstr == 0: continue
        elif istr == jstr: continue
        elif istr[1] == jstr[0]:
            istr= istr[0]
            jstr = jstr[1]
        else: continue
        inew = int(istr)
        jnew = int(jstr)
        if i*jnew == j*inew:
            numer.append(inew)
            denom.append(jnew)
print(numer)
print(denom)

