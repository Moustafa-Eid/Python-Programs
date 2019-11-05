import random
heads = 0
tails = 0
for count in range(0,300):
    coin = random.randint(0,1)
    if coin == 0:
        heads += 1
    elif coin == 1:
        tails += 1
print ("In 300 coin tosses heads was tossed %i times and tails was tossed %i times." % (heads, tails))

    