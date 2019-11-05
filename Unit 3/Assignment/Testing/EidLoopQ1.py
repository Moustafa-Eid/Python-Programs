# Name: Moustafa Eid
# Date: May 8 2017
# Class: ICS3U1-03
# Description: Repetition Assignment - Calculate Lean , Fat and Jack Sprat Numbers

# Function That checks if a number is Lean
def isLean(n, t):
    if t == n + 1:
        return True
    else:
        return False

# Function That checks if a number is Fat
def isFat(n, t):
    if t > 3*n:
        return True
    else:
        return False

# Function That checks if a number is Jack Sprat
def isJackSprat(n, t, t2):
    if t == n+1 and t2 > 3*(n+1):
        return True
    else:
        return False

# Input for number that will be checked
num = int(input("Please enter a number: "))

# Declaring the accumulator variables
total = 0
total2 = 0
total3 = 0
total4 = 0

# Creating a list to store the Jack Sprat Numbers
isSprat = []

# Loop that checks if a number is Lean
for factor in range(1,num+1):
    if num % factor == 0:
        total += factor

# Loop that checks if a number is Fat
for factor in range(1,num+2):
    if (num+1) % factor == 0:
        total2 += factor

# If statements that checks if the number is Lean and prints it out 
if isLean(num,total) == True:
    print ("Lean: Yes")
elif isLean(num,total) == False:
    print ("Lean: No")

# If statements that checks if the number is Fat and prints it out 
if isFat(num,total) == True:
    print ("Fat: Yes")
elif isFat(num,total) == False:
    print ("Fat: No")

# If statements that checks if the number is Jack Sprat and prints it out 
if isJackSprat(num, total, total2) == True:
    print ("Jack Sprat: Yes")
elif isJackSprat(num, total, total2) == False:
    print ("Jack Sprat: No")

# Prints Text before Jack Sprat Numbers
print ("These are the Jack Sprat Numbers from 1 - 10000")

# Loop That counts all the Jack Sprat numbers from 1-10000
for count in range (2,10001):
    if count != 1:  # Exception to make program more efficient
        if count % 2 != 0:  # Exception to make program more efficient
            if count % 3 != 0:  # Exception to make program more efficient
                if count % 5 != 0:  # Exception to make program more efficient
                    if count % 7 != 0:  # Exception to make program more efficient
                        isPrime = True #Checks if count is prime
                        for factor in range(2,int(count**0.5) + 1):
                                if count % factor == 0:
                                    isPrime = False # If count is not prime it breaks loop
                                    break 
                        for factor in range (2,count+2):    # Checks if number is Fat
                            if (count+1) % factor == 0:
                                total4 += factor # Accumulates Factors for Fat Numbers
                        if isPrime and total4 > 3*(count + 1):
                            isSprat.append(count) # Append that adds all the Jack Sprat Numbers calculated to the list
                        # Resetting variable back to 0 for the while loop to restart
                        total3 = 0
                        total4 = 0                   

# Prints All the Jack Sprat Numbers in the list
print (isSprat)