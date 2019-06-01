# Project Euler Problem 29

# import libraries here

powers = {4}

for a in range(2,101):
    for b in range(2,101):
        powers.add(a**b)

print(len(powers))
