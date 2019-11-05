# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: Distance between 2 coordinates using formula Sqrt((x2-x1)^2 + (y2-y1)^2))
import math

# Asks user for all the values for the coordiantes
xco1 = int(input("Please enter the X value for the 1st coordinate ")) 
yco1 = int(input("Please enter the Y value for the 1st coordinate ")) 
xco2 = int(input("Please enter the X value for the 2nd coordinate "))
yco2 = int(input("Please enter the Y value for the 2nd coordinate ")) 

# Calculation using distance formula
formula_1 = xco2 - xco1 # 1st part of formula, (x2-x1)
formula_2 = yco2 - yco1 # 2nd part of formula, (y2-y1)
formula_3 = formula_1**2 # 3rd part of formula (x2-x1)^2
formula_4 = formula_2**2 # 4th part of formula (y2-y1)^2
formula_5 = formula_3 + formula_4 # 5th part of the formula ((x2-x1)^2 + (y2-y1)^2))
final_answer = round(math.sqrt(formula_5),2) # 6th Part of formula Sqrt((x2-x1)^2 + (y2-y1)^2)) and final answer

# Printing the distance calculated in a sentence
print ("The distance between the 2 coordinates is",final_answer,"units.") 
