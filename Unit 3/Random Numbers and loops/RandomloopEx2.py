import random
dice5 = 0
for count in range(0,1000):
    dice = random.randint(1,6)
    if dice == 5:
        dice5 += 1
print ("In 1000 dice rolls the number 5 was rolled %i times." % (dice5))

    