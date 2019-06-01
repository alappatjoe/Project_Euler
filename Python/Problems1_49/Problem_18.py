# Project Euler Problem 18

f = open("p18.txt","r")
f1 = f.readlines()
triangle = []
for str in f1:
    num = str.split()
    for i in range(len(num)):
        num[i] = int(num[i])
    triangle.append(num)
    print(num)

for j in range(len(triangle) - 2, -1, -1):
    for k in range(len(triangle[j])):
        triangle[j][k] += max(triangle[j+1][k], triangle[j+1][k+1])

for row in triangle:
    print(row)

print(triangle[0][0])
