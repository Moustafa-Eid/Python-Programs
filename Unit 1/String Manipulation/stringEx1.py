# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: Program that Stores the price of three items and prints it in reciept form

#input gets name
name = input("Please enter your name: ")

#finds first and last name
first = (name[0:name.find(' ')])
last = (name[name.find(' ')+1:len(name)])

# prints last then first
print (last.upper()+",",first)
