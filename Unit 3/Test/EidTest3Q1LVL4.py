# Name: Moustafa Eid
# Date: April 16th 2017
# Class: ICS3U1-03
# Description: Calculates average word length

# Declares variables used as counters or accumulators
count = 0
length = 0
noun = 0

# While loop that runs program
while True:
    # The input that the user enters
    sentence = input("Enter word (or 999 to exit): ")
    # Checks if the input is all letters
    if sentence.isalpha() == True:
        # Checks if the word is a noun, if it is it doesnt count it
        if sentence[0:1].isupper() == False:
            # Calculates the total length of words and how many times the loop ran
            length += len(sentence)
            count += 1
        elif sentence[0:1].isupper() == True:
            noun += 1
    # if user enters 999 the loop ends
    if sentence == "999":
        break

# average is calculated by dividing length by how many times the loop ran
if count != 0:
    average = length / count
else:
    average = 0

# Prints the average and the number of proper nouns entered
print ("The average word length is %.2f." % (average))
print ("%i proper noun was entered." % (noun))
