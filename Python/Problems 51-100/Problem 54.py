# Project Euler Problem 54: Parsing cards for poker

# import libraries here


f = open("p54.txt")
f1 = f.readlines()
f.close()

def sortHand(hand):
    for i in range(len(hand)-1):
        min = hand[i][0]
        for j in range(i+1,len(hand)):
            if hand[j][0] < min:
                min = hand[j][0]
                hand.insert(i,hand.pop(j))
    return hand

games = []
for line in f1:
    cards = line.split()
    values = []
    for card in cards:
        num = 1
        if card[0] == 'T':
            num = 10
        elif card[0] == 'J':
            num = 11
        elif card[0] == 'Q':
            num = 12
        elif card[0] == 'K':
            num = 13
        elif card[0] == 'A':
            num = 14
        else: num = int(card[0])
        values.append([num,card[1]])
    hands = [sortHand(values[:5]), sortHand(values[5:])]
    games.append(hands)

def uniqueNums(hand):
    vals = []
    count = []
    for i in range(len(hand)):
        num = hand[i][0]
        if num in vals:
            count[vals.index(num)] += 1
        else:
            vals.append(num)
            count.append(1)

    return [vals, count, len(vals)]

def uniqueSuits(hand):
    suits = set()
    for card in hand:
        suits.add(card[1])

    return len(suits)

# full house - 7
# four of a kind - 8
def twoNums(vals, count, suits):
    if 2 in count:
        score = [7, vals[count.index(3)]]
    else:
        score = [8, vals[count.index(4)]]
    return score

# two pairs - 3
# three of a kind - 4
def threeNums(vals, count, suits):
    if 2 in count:
        if count.index(1) == 2:
            score = [3, vals[1], vals[0], vals[2]]
        else:
            pairIndex = count.index(2)
            score = [3, vals[2], vals[pairIndex], vals[1-pairIndex]]
    else:
        score = [4, vals[count.index(3)]]
    return score

# one pair - 2
def fourNums(vals, count, suits):
    pairCard = vals.pop(count.index(2))
    score = [2, pairCard, vals[-1], vals[-2], vals[-3]]
    return score

# high card - 1
# straight - 5
# flush - 6
# straight flush - 9
# royal flush - 10 (covered in straight flush)
def fiveNums(vals, count, suits):
    straight = False
    flush  = False

    if vals[4] - vals[0] == 4:
        straight = True
    elif vals[0] == 2 and vals[3] == 5 and vals[4] == 14:
        straight = True
        vals.insert(0, vals.pop(4)%13)

    if suits == 1: flush = True

    if straight == True:
        if flush == True:
            score = [9, vals[0]]
        else:
            score = [5, vals[0]]
    elif flush == True:
        score = list(vals)
        score.reverse()
        score.insert(0,6)
    else:
        score = list(vals)
        score.reverse()
        score.insert(0,1)

    return score

def scoreHand(hand):
    nums = uniqueNums(hand)
    suits = uniqueSuits(hand)

    #print(nums)
    #print(suits)

    switchNums = {
        2: twoNums,
        3: threeNums,
        4: fourNums,
        5: fiveNums
        }
    scoring = switchNums[nums[2]]
    score = scoring(nums[0], nums[1], suits)
    return score

p1Wins = 0
p2Wins = 0
for game in games:
    #print(game)
    p1Score = scoreHand(game[0])
    p2Score = scoreHand(game[1])
    if p1Score[0] > p2Score[0]: p1Wins += 1
    elif p1Score[0] == p2Score[0]:
        p1Score.pop(0)
        p2Score.pop(0)
        for i in range(len(p1Score)):
            if p1Score[i] == p2Score[i]: continue
            elif p1Score[i] > p2Score[i]:
                p1Wins += 1
                break
            else:
                p2Wins += 1
                break
    else: p2Wins += 1
    #print(p1Wins, p2Wins)

print("Player 1 Wins:", p1Wins)
print("Player 2 Wins:", p2Wins)

#print(games[0][0])
#print(uniqueSuits(games[0][0]))










