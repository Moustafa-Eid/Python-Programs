names = []
weeds = []

total = 0
count = 0
while True:
    name = input ("Please enter the 8 Kids names 1 by 1: ")
    weed = int(input("Please enter how many weeeds that person pulled: "))
    total += weed
    names.append(name)
    weeds.append(weed)
    count += 1
    if count == 8:
        break
    
for price in range(8):
    pay = (total / weeds[price])
    print ("%s got paid $%.2f" % (names[price],pay))
    pay = 0
    wage = 0