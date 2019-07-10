# Project Euler Problem 42

# import libraries here

f = open("p42.txt")
words = f.readline()[1:][:-1].split('","')
f.close()

def isTriangleNum(num):
    triNum = 1
    n = 1
    while triNum <= num:
        triNum = n*(n+1)/2
        n += 1
        if num == triNum: return True
    return False

triWords = []
for word in words:
    sum = 0
    for letter in word:
        sum += ord(letter) - 64
    if isTriangleNum(sum): triWords.append(word)

print(len(triWords))
