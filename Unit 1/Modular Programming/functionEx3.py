# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: Distance between 2 coordinates using formula Sqrt((x2-x1)^2 + (y2-y1)^2))

import math

#Defining Functions for Slope and Distance
def distance (xco1, yco1, xco2, yco2):
    return math.sqrt(((xco2-xco1)**2)+((yco2-yco1)**2))

def slope (xco1, yco1, xco2, yco2):
    return float((yco2-yco1)/(xco2-xco1))

# Asks user for all the values for the coordiantes
co1 = input("Enter the first coordinate: ")
co2 = input("Enter the second coordinate: ")

# Finds and seperates coordinates from user
xco1 = float(co1[co1.find(':')+1:co1.find(' ')])
yco1 = float(co1[co1.find(' ')+1:len(co1)])

xco2 = float(co2[co2.find(':')+1:co2.find(' ')])
yco2 = float(co2[co2.find(' ')+1:len(co2)])

# Variable vFor Storing Answers
final_slope = slope (xco1, yco1, xco2, yco2)
final_distance = distance(xco1, yco1, xco2, yco2)

# Printing the Distance and Slope calculated in a sentence
print ("The distance between points (%i,%i) and (%i,%i) is %.3f." % (xco1, yco1, xco2, yco2, final_distance))
print ("The slope between points (%i,%i) and (%i,%i) is %.3f." % (xco1, yco1, xco2, yco2, final_slope))
