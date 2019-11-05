import random
count = 0
winningnum = 0
roll = 0
print ("Welcome to Craps!")
while (True):
    dice1 = random.randint(1,6)    
    dice2 = random.randint(1,6)
    dicetotal = dice1 + dice2
    count += 1
    if count == 1:
        if dicetotal == 7 or dicetotal == 11:
            print ("You rolled a %i and a %i." % (dice1,dice2))
            print ("Your total = %i" % (dicetotal))
            print ("Congratulations you won! because you total was either 7 or 11")
            break
        elif dicetotal == 2 or dicetotal == 3 or dicetotal == 12:
            print ("You rolled a %i and a %i." % (dice1,dice2))
            print ("Your total = %i" % (dicetotal))
            print ("Im sorry you lost because you total was either 2 or 3 or 11")
            break
        else:
            print ("You rolled a %i and a %i." % (dice1,dice2))
            print ("Your total = %i" % (dicetotal))
            print ("Keep Rolling!")
            winningnum = dicetotal            
    if count != 1:
        roll += 1
        print ("Roll #%i." % (roll))
        if dicetotal == 7:
            print ("You rolled a %i and a %i." % (dice1,dice2))
            print ("Your total = %i" % (dicetotal))
            print ("Im sorry you lost because you rolled a 7.")
            break
        elif dicetotal == winningnum:
            print ("You rolled a %i and a %i." % (dice1,dice2))
            print ("Your total = %i" % (dicetotal))
            print ("Congratulations you won! because you rolled your winning number %i!." % (winningnum))
            break
            
            
            