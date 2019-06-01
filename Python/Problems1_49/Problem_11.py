# Project Euler Problem 11

f = open("p11.txt", "r")
f1 = f.readlines()
n = []
num = 0
for i in range(len(f1)):
    list = []
    for j in range(20):
        num = int(f1[i][3*j:3*j + 2])
        list.append(num)
    n.append(list)


prod = 1
temp = 1
right = True
down = True
left = True
for k in range(20):
    for l in range(20):
        print(k,l)
        down = (k+3 < 20)
        right = (l+3 < 20)
        left = l>2
        if right:
            temp = n[k][l]*n[k][l+1]*n[k][l+2]*n[k][l+3]
            #print(k, l, temp)
            if temp > prod:
                prod = temp
        if down:
            temp = n[k][l]*n[k+1][l]*n[k+2][l]*n[k+3][l]
            #print(k, l, temp)
            if temp > prod:
                prod = temp
        if right and down:
            temp = n[k][l]*n[k+1][l+1]*n[k+2][l+2]*n[k+3][l+3]
            #print(k, l, temp)
            if temp > prod:
                prod = temp
        if left and down:
            temp = n[k][l]*n[k+1][l-1]*n[k+2][l-2]*n[k+3][l-3]
            #print(k, l, temp)
            if temp > prod:
                prod = temp

print(prod)

