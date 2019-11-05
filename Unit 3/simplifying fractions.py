fraction = input("Please enter a fraction in the form (a/b): ")
numerator = int(fraction[0:fraction.find('/')])
denominator = int(fraction[fraction.find('/')+1:len(fraction)])

if denominator > numerator:
    for factor in range(1,numerator+1):
        if numerator % factor == 0:
            numerator /= factor
            denominator /= factor
            
if numerator > denominator:
    for factor in range(1,denominator+1):
        if denominator % factor == 0:
            numerator /= factor
            denominator /= factor
            
print ("%i/%i" % (numerator,denominator))
    
