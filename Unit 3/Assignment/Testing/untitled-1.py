def Loopall (n1,n2,t):
    for factor in range (1,n1):
        if n2 % factor == 0:
            t += factor
            
