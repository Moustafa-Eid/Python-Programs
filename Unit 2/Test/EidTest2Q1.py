# Name: Moustafa Eid
# Date: April 13th 2017
# Class: ICS3U1-03
# Description: Chings printing cost calculation

# Input for papertype and how many copies
papertype = input("Would you like black & white or colour? ").lower()
copies = int(input("How many copies would you like? "))

# Constants for price of each copy in different circumstances
BW_1TO100 = 0.1
BW_101TO500 = 0.08
BW_501PLUS = 0.05
C_1TO100 = 0.8
C_101TO500 = 0.6
C_501PLUS = 0.4

#Tax On purchase
TAX = 1.06

#If statement to check which papertype it is and then check how many copies and calculate price
if papertype == "black and white" or papertype == "black & white" or papertype == "b/w":
    if copies >= 1 and copies <= 100:
        price = copies * BW_1TO100
        copyprice = BW_1TO100
    elif copies >= 101 and copies <= 500:
        price = copies * BW_101TO500
        copyprice = BW_101TO500
    elif copies >= 501:
        price = copies * BW_501PLUS
        copyprice = BW_501PLUS        
    else:
        print ("Invalid Input")
elif papertype == "colour" or papertype == "color" or papertype == "c":
    if copies >= 1 and copies <= 100:
        price = copies * C_1TO100
        copyprice = C_1TO100        
    elif copies >= 101 and copies <= 500:
        price = copies * C_101TO500
        copyprice = C_101TO500        
    elif copies >= 501:
        price = copies * C_501PLUS
        copyprice = C_501PLUS                
    else:
        print ("Invalid Input")

# If Statement to calculate shipping price  
if price <= 50:
    delivery = 5
elif price > 50:
    delivery = 0
else:
    ("Invalid Input")
    
# Calculates cost of everything in total
cost = (price + delivery) * TAX
taxtotal = (price + delivery) * 0.06
subtotal = price + delivery
# Outputs answer
print ("Copies\t\t%i * %.2f = %10.2f" % (copies,copyprice,price))
print ("delivery%31.2f" % (delivery))
print ("\t\t\t\t-------")
print ("SUBTOTAL%31.2f" % (subtotal))
print ("GST(6%%)%32.2f" % (taxtotal))
print ("\t\t\t\t-------")
print ("TOTAL%34.2f" % (cost))





 