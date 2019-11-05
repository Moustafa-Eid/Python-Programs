# Asks for location and lowers it
location = input ("Where are you mailing to: ").lower()

# If Statement to look at location and figure out price
if location == "canada":
    price = 0.52
    package = "mailing within Canada"
elif location == "united States of america" or location == "america" or location == "usa" or location == "us":
    price = 0.93
    package = "mailing to USA"
else:
    price = 1.55
    package = "mailing Internationally"
    
# outputs answer to user with price
print ("The Postage will cost you $%.2f because you are %s." % (price,package))
