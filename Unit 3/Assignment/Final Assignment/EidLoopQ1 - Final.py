# Name: Moustafa Eid
# Date: May 8 2017
# Class: ICS3U1-03
# Description: Repetition Assignment - Calculate Lean , Fat and Jack Sprat Numbers

import timeit

# Function That checks if a number is Lean
def isLean(n):
    global isPrime
    if n == 0:
        isPrime = False
    else:
        isPrime = True #Checks if count is prime
        for factor in range(2,int(n**0.5) + 1):
            if n % factor == 0:
                isPrime = False # If count is not prime it breaks loop
                break
    return isPrime


# Function That checks if a number is Fat
def isFat(n,t):
    for factor in range(1,n+1):
        if n % factor == 0:
            t += factor
    if t > (3*n):
        return True
    else:
        return False

# Function That checks if a number is Jack Sprat
def isJackSprat(n,n1,t):
    if isLean(n):
        if isFat(n1,t):
            return True
    else:
        return False

# Declaring constant for JackSprat
JACK_SPRAT_MAX = 1000

# Declaring the accumulator variables
total = 0

# Declaring Variable to store list
isSprat = []


# Prints Text before Jack Sprat Numbers
print ("These are the Jack Sprat Numbers from 1 - 10000")

# Starts a Timer
start = timeit.default_timer()

# For loop to print all the Jack Sprat Numbers from 1 - 10000
for count in range(1,JACK_SPRAT_MAX + 1, 2):
    if isJackSprat(count,count+1,total):
        isSprat.append(count)   # Appending all the Jack Sprat Numbers to the list

# Outputting the list that stores all Jack Sprat Numbers
print (isSprat)

# Stops the timer
stop = timeit.default_timer()

# Prints the time it took to print jacksprat numbers
print ("The Time it took to print the Jack Sprat Numbers is %.2f seconds." % (stop - start))

# Input for number that will be checked
num = int(input("Please enter a number to check if is it Lean, Fat or Jack Sprat: "))

# If statements that checks if the number is Lean and prints it out 
if isLean(num) == True:
    print ("Lean: Yes")
elif isLean(num) == False:
    print ("Lean: No")

# If statements that checks if the number is Fat and prints it out 
if isFat(num,total) == True:
    print ("Fat: Yes")
elif isFat(num,total) == False:
    print ("Fat: No")

# If statements that checks if the number is Jack Sprat and prints it out 
if isJackSprat(num,num+1, total):
    print ("Jack Sprat: Yes")
else:
    print ("Jack Sprat: No")



