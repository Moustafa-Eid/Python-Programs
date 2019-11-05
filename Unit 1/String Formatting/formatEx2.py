# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: Program that Stores the price of three items

# Declaring Price Variables
price1 = 2.55
price2 = 3.20
price3 = 4.00

# Calculating Total Cost
total = price1 + price2 + price3

# Printing Format + Answer
print ("Item one:%8.2s%5.2f" % ("$", price1))
print ("Item two:%8.2s%5.2f" % ("$", price2))
print ("Item three:%6.2s%5.2f" % ("$", price3))
print ("%23s" % ("-------"))
print ("Total cost%7.2s%5.2f" % ("$", total))