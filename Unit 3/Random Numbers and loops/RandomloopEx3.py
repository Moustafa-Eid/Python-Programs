# Name: Moustafa Eid
# Date: April 27th 2017
# Class: ICS3U1-03
# Description: checks if 2 coins are the same

import random
#Declares variable
coinsim = 0

#Loop that flips 2 coins then checks if they are the same
for count in range(0,10000):
    coin1 = random.randint(0,1)
    coin2 = random.randint(0,1)
    if coin1 == coin2:
        coinsim += 1

# Outputs the results
print ("In 10000 coin tosses coin 1 and 2 were the same %i times." % (coinsim))

    