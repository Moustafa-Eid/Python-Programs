# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: Program that Stores the price of three items and prints it in reciept form

# Asking user for Names and Prices of products
item1_name = input("Please enter the name of the first product: ")
item1_price = float(input("Please enter the price of the first product: $"))
item2_name = input("Please enter the name of the second product: ")
item2_price = float(input("Please enter the price of the second product: $"))
item3_name = input("Please enter the name of the third product: ")
item3_price = float(input("Please enter the price of the third product: $"))

# Calculating Tax
TAX_RATE = 0.13
tax = (item1_price + item2_price + item3_price) * TAX_RATE
tax_title = "HST (13%)"
# Adding Tax
total = item1_price + item2_price + item3_price + tax

# Printing The Reciept with the right format
print (" ")
print ("WOSS Gift Shop Receipt")
print ("----------------------")
print ("\n%-15s%s%5.2f" % (item1_name, "$", item1_price)) 
print ("%-15s%s%5.2f" % (item2_name, "$", item2_price)) 
print ("%-15s%s%5.2f" % (item3_name, "$", item3_price))
print ("%22s" % ("-------"))
print ("%-15s%s%5.2f" % (tax_title,"$", tax))
print ("%22s" % ("-------"))
print ("TOTAL%11s%5.2f" % ("$", total))



