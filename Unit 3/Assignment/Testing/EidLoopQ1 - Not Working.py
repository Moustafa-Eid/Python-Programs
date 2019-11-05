def loop (x,y,z,t):
    for factor in range (x,y):
        if factor % 2 != 0:
            if y % factor == 0:
                t += factor
    return t

def isLean(n, t):
    if t == n + 1:
        return True
    else:
        return False

def isFat(n, t):
    if t > 3*num:
        return True
    else:
        return False
    
def isJackSprat(n, t, t2):
    if t == n+1 and t2 > 3*(n+1):
        return True
    else:
        return False

num = int(input("Please enter a number: "))

total = 0
total2 = 0
total3 = 0
total4 = 0

loop (1,num+1,num,total)
loop (1,num+2,num+1,total2)

if isLean(num,total) == True:
    print ("Lean: Yes")
elif isLean(num,total) == False:
    print ("Lean: No")
    
if isFat(num,total) == True:
    print ("Fat: Yes")
elif isFat(num,total) == False:
    print ("Fat: No")
    
if isJackSprat(num, total, total2) == True:
    print ("Jack Sprat: Yes")
elif isJackSprat(num, total, total2) == False:
    print ("Jack Sprat: No")
    
print ("These are the Jack Sprat Numbers from 1 - 1000")

for count in range (1,1001):
    if count % 2 != 0:
        loop (1,count+1,count,total3)
        loop (1,count+2,count+1,total4)
    if isLean(count,total3) and isFat(count+1,total4):
        print (count)
    total3 = 0
    total4 = 0
        
