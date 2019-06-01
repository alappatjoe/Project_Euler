# Project Euler Problem 13

f = open("p13.txt", "r")
f1 = f.readlines()
n = []
num = 0
for i in range(len(f1)):
    list = []
    for j in range(50):
        #print(i,j,f1[i][j])
        num = int(f1[i][49-j])
        list.append(num)
    n.append(list)

sums = []
for l in range(len(n[1])):
    #print(l)
    sums.append(0)
    for k in range(len(n)):
        sums[l] += n[k][l]

carry = 0
sum = ""
temp = 0
for m in range(len(sums)+2):
    if m < 1:
        if m == 0:
           # print(m, sums[m])
            sum += str(sums[m]%10)
        else:
            temp = sums[m]%10 + int(sums[m-1]/10)%10
            sum += str(temp%10)
            carry = int(temp/10)
    elif m >= len(sums):
        if m == len(sums):
            temp = carry + int(sums[m-1]/10)%10 + int(sums[m-2]/100)
            sum += str(temp%10)
            carry = int(temp/10)
        else:
            temp = carry + int(sums[m-2]/100)
            sum += str(temp)[::-1]
    else:
        temp = carry + sums[m]%10 + int(sums[m-1]/10)%10 + int(sums[m-2]/100)
        sum += str(temp%10)
        carry = int(temp/10)

print(sum[-1:-11:-1])
