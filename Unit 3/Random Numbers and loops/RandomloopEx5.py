import random

suit = random.choice(['Hearts','Diamonds','Clubs','Spades'])
number = random.randint (1,13)

if number > 1 and number <= 10:
    print ("The card you picked is a %i of %s." % (number,suit))
elif number == 1:
    print ("The card you picked is a Ace of %s." % (suit))
elif number == 11:
    print ("The card you picked is a Jack of %s." % (suit))
elif number == 12:
    print ("The card you picked is a King of %s." % (suit))
elif number == 13:
    print ("The card you picked is a Queen of %s." % (suit))