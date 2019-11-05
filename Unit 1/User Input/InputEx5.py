# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: Calculate slices of pizza for a party

SLICES = 32 # total slices available

guests = int(input("How many people are coming to the party that are going to eat pizza? ")) # Asks user how many guests are attending
print ("Number of guests:",guests,) # states number of guests

# Calculations for Option 1
op1_1 = SLICES // guests
op1_2 = SLICES / guests
op1_3 = op1_2 - op1_1
op1_4 = round(float(op1_3 * guests),1)
op1_4_1 = int(op1_4)
print ("Option 1:",op1_1,"slices each,",op1_4_1,"left over.") # Printing option 1

# Calculations for option 2
op2 = round(SLICES / guests,2)
print ("Option 2:",op2,"slices each.") # printing option 2
