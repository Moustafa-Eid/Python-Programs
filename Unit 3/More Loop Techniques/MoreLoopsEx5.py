# Name: Moustafa Eid
# Date: April 27th 2017
# Class: ICS3U1-03
# Description: product of odd digits

#Asks for a number as input
num = input("Please enter a number: ")
product = 1
dignum = 0

# Loop that checks if digit is odd then multiplys together
for count in num:
    if int(count) % 2 != 0:
        product = int(count) * product
        dignum += 1
        
#Prints output
if dignum == 0:
    print ("0")
elif dignum != 0:
    print (product)
