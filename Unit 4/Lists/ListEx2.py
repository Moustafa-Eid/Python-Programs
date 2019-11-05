fruits = ['Strawberries','Grapes','Peaches','Apples','Cherries','Dragon Fruit','Pineapples','Banana','Apricots','Oranges']
price = [3,10,7,5,13,30,17,6,12,9]

print ("\tMoustafa's Fruit Shop")
print ("\t---------------------")
for count in range(10):
    print("      %-20s$%.2f" % (fruits[count],price[count]))