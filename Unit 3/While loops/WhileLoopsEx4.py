# Name: Moustafa Eid
# Date: April 27th 2017
# Class: ICS3U1-03
# Description: Checks how many times a number is divisible by 2

#Input to check for a number
num1 = int(input("Please enter a number: "))

#declaring variables
numout = num1
count = 0

#While loop that checks if a number is divisible by 2 then checks if its quotient is also divisible by 2 
while (True):
    if num1 % 2 == 0:
        num1 = num1 / 2
        count += 1
    else:
        break

#Prints output for program
print ("\n%i is divisible by 2, %i times." % (numout, count))
