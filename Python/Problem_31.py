# Project Euler Problem 31

# import libraries here

combinations = 0
max = 200

twoPound = max
while twoPound >= 0:
    onePound = twoPound
    while onePound >= 0:
        p50 = onePound
        while p50 >= 0:
            p20 = p50
            while p20 >= 0:
                p10 = p20
                while p10 >= 0:
                    p5  =p10
                    while p5 >= 0:
                        p2 = p5
                        while p2 >= 0:
                            combinations += 1
                            p2 -= 2
                        p5 -=5
                    p10 -= 10
                p20 -= 20
            p50 -= 50
        onePound -= 100
    twoPound -= 200

print(combinations)