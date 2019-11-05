import random
number = random.randint (1,100)
count = 0
while (True):
    guess = int(input("Please choose a number from 1-100: "))
    count += 1
    if guess > number:
        print ("Too High!")
    elif guess < number:
        print ("Too Low!")
    elif guess == number:
        print ("Congratulations! you Guessed the correct number in %i turns!." % (count))
        break