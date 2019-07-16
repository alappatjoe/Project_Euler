# Project Euler Problem 59

import Timer

def encryption(text, key):
    keyLength = len(key)
    encrypted = [None for x in range(len(text))]
    for i in range(len(text)):
        encrypted[i] = text[i]^ord(key[i%keyLength])
    
    return encrypted

f = open("p59.txt")
f1 = f.readline().split(",")
f.close()

input = []

#splitf1 = [[],[],[]]
for i in range(len(f1)):
    #splitf1[i%3].append(f1[i])
    input.append(int(f1[i]))

#nums1 = []
#count1 = []
#for i in range(len(splitf1[0])):
#    if splitf1[0][i] in nums1:
#        count1[nums1.index(splitf1[0][i])] += 1
#    else:
#        nums1.append(splitf1[0][i])
#        count1.append(1)

#nums2 = []
#count2 = []
#for i in range(len(splitf1[1])):
#    if splitf1[1][i] in nums2:
#        count2[nums2.index(splitf1[1][i])] += 1
#    else:
#        nums2.append(splitf1[1][i])
#        count2.append(1)

#nums3 = []
#count3 = []
#for i in range(len(splitf1[2])):
#    if splitf1[2][i] in nums3:
#        count3[nums3.index(splitf1[2][i])] += 1
#    else:
#        nums3.append(splitf1[2][i])
#        count3.append(1)

#print(nums1)
#print(count1)
#print("")
#print(nums2)
#print(count2)
#print("")
#print(nums3)
#print(count3)
#print("")

# 69  88  80

#spaces = [69, 88, 80]
#espaces = encryption(spaces, " ")
#print(espaces)
#print(chr(espaces[0]), chr(espaces[1]), chr(espaces[2]))

output = encryption(input, "exp")
sum = 0
for j in range(len(output)):
    sum += output[j]
    output[j] = chr(output[j])
final = "".join(output)
print(final)
print(sum)



