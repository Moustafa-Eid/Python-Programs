# Name: Moustafa Eid
# Date: April 11th 2017
# Class: ICS3U1-03
# Description: Find If 2 lines are parallel, same or intersecting and output result of P.O.I and Quadrant
# Giving Variables a starting value
slope1 = 0
slope2 = 0
y1 = 0
y2 = 0

# Input for 2 Equations in (y = mx + b) form
equation1 = input("Enter the Equation 1 formula (y= mx + b): ")
equation2 = input("Enter the Equation 2 formula (y= mx + b): ")

# Variables For finding if there is a yint or not and its sign
eqyint1 = equation1[equation1.find('x'):len(equation1)]
eqyint2 = equation2[equation2.find('x'):len(equation2)]

# Finds if equation 1 has a y int and then finds slope
if equation1.find('y') != 0 and equation1.find('=') != 1:
    print ("Equation 1 is Invalid")
else:
    if eqyint1.count("+") == 1 or eqyint1.count("-") == 1:
        if equation1[equation1.find(' '):equation1.find('x')] == ' ':
            slope1 = 1
            if "+" in eqyint1:
                y1 = float(equation1[equation1.find('+')+1:len(equation1)])                    
            elif "-" in eqyint1:
                y1 = (float(equation1[equation1.find('x')+3:len(equation1)])) * -1
        elif equation1[equation1.find(' '):equation1.find('x')] == ' -':
            slope1 = -1
            if "+" in eqyint1:
                y1 = float(equation1[equation1.find('+')+1:len(equation1)])                    
            elif "-" in eqyint1:
                y1 = (float(equation1[equation1.find('x')+3:len(equation1)])) * -1 
        elif equation1[equation1.find(' '):equation1.find('x')] != ' ':
            slope1 = float(equation1[equation1.find(' '):equation1.find('x')])
            if "+" in eqyint1:
                y1 = float(equation1[equation1.find('+')+1:len(equation1)])                    
            elif "-" in eqyint1:
                y1 = (float(equation1[equation1.find('x')+3:len(equation1)])) * -1     
    # Finds if Equation 1 does not have a y int then finds slope
    if eqyint1.count("+") == 0 and eqyint1.count("-") == 0:
        if equation1[equation1.find(' '):equation1.find('x')] == ' ':
            slope1 = 1
            y1 = 0
        elif equation1[equation1.find(' '):equation1.find('x')] == ' -':
            slope1 = -1
            y1 = 0
        elif equation1[equation1.find(' '):equation1.find('x')] != ' ':
            slope1 = float(equation1[equation1.find(' '):equation1.find('x')])
            y1 = 0
        
if equation2.find('y') != 0 and equation2.find('=') != 1:
    print ("Equation 2 is Invalid")
else:
    #Finds if Equation 2 has a y int and finds slope
    if eqyint2.count("+") == 1 or eqyint2.count("-") == 1:
        if equation2[equation2.find(' '):equation2.find('x')] == ' ':
            slope2 = 1
            if "+" in eqyint2:
                y2 = float(equation2[equation2.find('+')+1:len(equation2)])                    
            elif "-" in eqyint2:
                y2 = (float(equation2[equation2.find('x')+3:len(equation2)])) * -1
        elif equation2[equation2.find(' '):equation2.find('x')] == ' -':
            slope2 = -1
            if "+" in eqyint2:
                y2 = float(equation2[equation2.find('+')+1:len(equation2)])                    
            elif "-" in eqyint2:
                y2 = (float(equation2[equation2.find('x')+3:len(equation2)])) * -1        
        elif equation2[equation2.find(' '):equation2.find('x')] != ' ':
            slope2 = float(equation2[equation2.find(' '):equation2.find('x')])
            if "+" in eqyint2:
                y2 = float(equation2[equation2.find('+')+1:len(equation2)])                    
            elif "-" in eqyint2:
                y2 = (float(equation2[equation2.find('x')+3:len(equation2)])) * -1
        
    #Finds if Equation2 does not have a y int and finds slope
    if eqyint2.count("+") == 0 and eqyint2.count("-") == 0:
        if equation2[equation2.find(' '):equation2.find('x')] == ' ':
            slope2 = 1
            y2 = 0
        elif equation2[equation2.find(' '):equation2.find('x')] == ' -':
            slope2 = -1
            y2 = 0
        elif equation2[equation2.find(' '):equation2.find('x')] != ' ':
            slope2 = float(equation2[equation2.find(' '):equation2.find('x')])
            y2 = 0    
    
if equation1.find('y') == 0 and equation1.find('=') == 1 and equation2.find('y') == 0 and equation2.find('=') == 1:
    # Finds if it is parallel or same or intersecting then calculates point of intersection and quadrant of that point           
    if slope1 == slope2 and y1 != y2:
        print ("These 2 lines are parallel")
    elif slope1 == slope2 and y1 == y2:
        print ("These 2 lines are the same")
    else:
        print ("The 2 lines will intersect")
        step1 = slope2 - slope1
        step2 = y1 - y2
        x = step2/step1
        y = (slope1*x)+y1
        
        if x > 0 and y > 0:
            quadrant = "at Quadrant 1"
        elif x < 0 and y > 0:
            quadrant = "at Quadrant 2"
        elif x < 0 and y < 0:
            quadrant = "at Quadrant 3"
        elif x > 0 and y < 0:
            quadrant = "at Quadrant 4"
        elif x == 0 and y != 0:
            quadrant = "on the Y axis"
        elif x != 0 and y == 0:
            quadrant = "on the X axis"
        else:
            quadrant = "at the origin"
        
        #Outputs the Results
        print ("The Point of Intersection is (%.2f,%.2f)" % (x,y))
        print ("This Point of intersection is %s" % (quadrant))    
     
   


