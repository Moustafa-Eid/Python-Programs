# Asks for length and width
length = int(input("Please enter the length of the rectangle: "))
width = int(input("Please enter the width of the rectangle: "))

#calculations 
area = length * width
perimeter = (2*length) + (2*width)

# If Statement to decide what is bigger
if area > perimeter:
    print ("The Rectangle has an area greater than the perimeter")
elif area <  perimeter:
    print ("The Rectangle has an area less than the perimeter")
elif area == perimeter:
    print ("The Rectangle has an area equal to the perimeter")
