# Project Euler Problem 22

f = open("p22.txt")
names = f.readline().split(",")
f.close()

for j in range(len(names)):
    names[j] = names[j][1:][:-1]
names.sort()

totalScore = 0
for i in range(len(names)):
    score = 0
    for char in names[i]:
        score += ord(char) - 64
    print(i+1, names[i], score, score*(i+1), totalScore)
    score *= (i+1)
    totalScore += score

print(totalScore)

