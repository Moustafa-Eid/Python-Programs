num = int(input("Please enter a number: "))


isPrime = True
for factor in range(2,num):
            if num % factor == 0:
                        isPrime = False
    

if num == 1 or isPrime == False:
            print ("NO")        
elif isPrime == True:
            print ("Yes")

    