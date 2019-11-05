# Constant for tax
TAX = 0.08

# Input price of meal
price = float(input("Enter the price of the meal==> $"))

# If statement to change tax
if price > 4.00:
    totaltax = (price*TAX)
    total = totaltax + price
elif price <= 4.00 and price > 0.00:
    totaltax = 0
    total = totaltax + price

# Printing Reciept
print (" ")    
print ("McD's Receipt")
print ("-------------")
print (" ")
print ("%-17s%s%5.2f" % ("Meal", "$", price))
print ("\t\t-------")
print ("%-17s$%5.2f" % ("Tax (8%)",totaltax))
print ("\t\t-------")
print ("%-17s$%5.2f" % ("TOTAL",total))

