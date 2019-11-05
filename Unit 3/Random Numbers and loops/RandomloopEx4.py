import random
dicepoint = 0
count = 0
while (True):
    dice = random.randint(1,6)    
    if count == 0:
        dicepoint = dice
    count += 1
    if count > 1 and dice == dicepoint:
        print ("after %i rolls, side number %i was rolled again." % (count, dicepoint))
        break
    

    