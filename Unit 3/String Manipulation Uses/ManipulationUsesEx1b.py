entry = input ("Please enter a string: ")

if entry[0].isdigit() == True and entry[1:len(entry)+1].isalpha() == True and len(entry) >= 8:
    print ("The input meets all the requirements")
else:
    print ("The input does not meet all the requirements")