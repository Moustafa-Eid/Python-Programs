# Name: Moustafa Eid
# Date: April 27th 2017
# Class: ICS3U1-03
# Description: counting froom a number to the next number

# Input asking for 2 numbers
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

# If statement that looks for numbers in between the 2 inputs and then uses a loop to count everyrhing in between. 
if num1 < num2:
    for count in range(num1,num2+1):
        print (count)
elif num1 > num2:
    for count in range(num1,num2-1,-1):
        print (count)
else: 
    print (num1)