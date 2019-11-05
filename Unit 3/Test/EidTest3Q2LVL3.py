num = int(input("Enter a number: "))

odd = 1
total = 0

for sequence in range(1,num+1):
    total += odd
    odd += 2
    
print ("The sum is %i." % (total))

    
    
        
    