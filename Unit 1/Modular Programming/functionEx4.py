# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: Centres word in spaces given

import math

# Defining Functions for Dots calculation
def centre (spaces, word):
    dotscalculation = (spaces - len(word)) / 2
    return dotscalculation

# Asks user for input spaces and word
spaces = int(input("Please enter the number of spaces you want: "))
word = input("Please enter the word that is going to be centered: ")

# Casts function centre as integer
dots1 = int(centre(spaces, word))
dots2 = math.ceil(centre(spaces, word))

# Outputs the results
print ("."*dots1+word+"."*int(dots2))


            
