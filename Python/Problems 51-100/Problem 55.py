# Project Euler Problem 55

# import libraries here

def reverseNumber(num):
    reverse = 0
    while num > 0:
        reverse = (reverse*10) + num%10
        num //= 10
    return reverse

def palindrome(num):
    if reverseNumber(num) == num: return True
    return False

def lychrel(num):
    for i in range(50):
        num += reverseNumber(num)
        if palindrome(num): return False
    return True


count = 0
for i in range(10000):
    if lychrel(i): count += 1

print(count)


