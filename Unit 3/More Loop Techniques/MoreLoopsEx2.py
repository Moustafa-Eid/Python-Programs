num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
sum = 0

if num1 < num2:
    for count in range (num1+1,num2):
        sum = sum + count
elif num2 < num1:
    for count in range (num2+1,num1):
        sum = sum + count


print (sum)