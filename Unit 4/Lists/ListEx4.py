import random

ladderstart = [6,24,30,49,82]
ladderend = [17,26,44,62,86]
snakestart = [14,20,39,66,69,79,84,88]
snakeend = [3,15,33,53,58,67,71,36]

p1pos = 1
p2pos = 1
count = 0
count2 = 0

while True:
    player1 = input("Player 1 hit Enter to roll")
    if player1 == "":    
        diceroll = random.randint(1,6)
        print ("You rolled a %i" % (diceroll))
        p1pos += diceroll
        for ladder in ladderstart:
            if p1pos == ladder:
                p1pos = ladderend[count]
            count += 1
        count = 0
        for snake in snakestart:
            if p1pos == snake:
                p1pos = snakeend[count]
            count += 1
        print ("You are at spot %i" % (p1pos))
    
    player2 = input("Player 2 hit Enter to roll")
    if player2 == "":
        diceroll = random.randint(1,6)
        print ("You rolled a %i" % (diceroll))
        p2pos += diceroll
        for ladder in ladderstart:
            if p2pos == ladder:
                p2pos = ladderend[count]
            count += 1
        count = 0
        for snake in snakestart:
            if p2pos == snake:
                p2pos = snakeend[count]
            count += 1
        print ("You are at spot %i" % (p2pos))
    if p1pos == 90:
        print ("Player 1 won")        
        break
    if p2pos == 90:
        print ("Player 2 won")        
        break
    if p1pos > 90:
        p1pos -= diceroll
    if p2pos > 90:
        p2pos -= diceroll

    
    
        
    
                
                
    
    