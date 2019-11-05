# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: Currency converter (CAD) to (EUR)

#Input Canadian dollars
money = int(input("Please enter the amount of money in Canadian Dollars that you want to convert to euros "))

# Rate of change from cad to euro + converting from cad to euro
RATE = 0.721908 
conversion = round(money * RATE,2) 

#printing the results
print ("If you have $"+str(money),"(CAD) you can convert it to €"+str(conversion)+"(EUR).") 