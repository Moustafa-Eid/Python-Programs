# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: Program that Stores the price of three items and prints it in reciept form

#function that gets base and exponent and calculates it
def power(base, exponent):
    return base ** exponent

#input base and exponent
basenum = float(input("Enter the number for the base: "))
expnum = float(input("Enter the number for the bade: "))

#print the answer
print (power(basenum, expnum))