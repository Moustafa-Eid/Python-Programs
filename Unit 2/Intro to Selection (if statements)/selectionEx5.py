# Name: Moustafa Eid
# Date: April 11th 2017
# Class: ICS3U1-03
# Description: Calculates area needed for python enclosure

# Asks user for length of python
pysize = float(input("Please Enter The Size Of The Python: "))

# checks if number is bigger or smaller than 6 then calculates area
if pysize <= 6:
    area = (pysize * 0.5)
elif pysize > 6:
    pysizenew = (pysize - 6)
    area = (3 + (pysizenew * 0.75))
    
# Outputs Area Needed For Python
print ("The Python needs an area of %.2f square feet" % (area))
    