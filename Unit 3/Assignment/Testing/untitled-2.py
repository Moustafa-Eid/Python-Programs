
def isLean(num):
    if sum_factor (num) == num + 1:
        return True
    else:
        return False

def isFat(num):
    if sum_factor (num) > 3*num:
        return True
    else:
        return False
    
#def isJackSprat(n, t, t2):
    #if t == n+1 and t2 > 3*(n+1):
        #return True
    #else:
        #return False
    
def sum_factor (num):
    total = 0    
    for factor in range (2,(num//2) + 1):
        if num % factor == 0:
            total += factor
    return total

num = int(input("Please enter a number: "))

#total2 = 0
#total3 = 0
#total4 = 0
#prime = ""

        
if isLean(num) == True:
    print ("Lean: Yes")
elif isLean(num) == False:
    print ("Lean: No")
    
if isFat(num) == True:
    print ("Fat: Yes")
elif isFat(num) == False:
    print ("Fat: No")
    
#if isJackSprat(num, total, total2) == True:
    #print ("Jack Sprat: Yes")
#elif isJackSprat(num, total, total2) == False:
    #print ("Jack Sprat: No")


#print ("These are the Jack Sprat Numbers from 1 - 1000")

#for count in range (1,10000):
    #if count % 2 != 0:
        #for factor in range (2,((count//2)+1)):
            #if factor %  2 != 0:
                #if count % factor == 0:
                    #total3 += factor
        #for factor in range (1,((count//2)+2)):
            #if (count+1) % factor == 0:
                #total4 += factor 
        #if total3 == (count + 1) and total4 > 3*(count + 1):
            #prime = prime + str(count) + ", "
        #total3 = 0
        #total4 = 0

#print (prime[0:len(prime)-2])