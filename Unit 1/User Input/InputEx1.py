# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: User Input calculating area and circumference of circle

import math

# Inputing a radius value
radius = int(input("Please enter a radius ")) 

# Calculating Area and Circumference of Circle
area = round(math.pi * radius**2,1) # Calculating Area of Circle
circumference = round(2 * math.pi * radius,1) # Calculating Circumference of Circle

# Printing output
print ("A circle with radius",radius,"cm has an area of",area,"square centimetres and a circumference of",circumference,"cm.") # Printing the sentence that shows up on screen