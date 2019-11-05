# Name: Moustafa Eid
# Date: June 5th 2017
# Class: ICS3U1-03
# Description: Lists Test - Pollution

# Opens text file
numFile = open("pollution.txt", "r")

# Creates all lists used in program
pollution = []
day = []
peaks = []
peaksday = []

# Creates all counter and accumulator variables used
count = 0
big = 0
peaksoutput = ""

# While loop that reads each line of code and appends the numbers to a list with their day
while True:
    num = numFile.readline()    # Reads text file
    if num == "":
        break
    pollution.append(int(num[:-1])) # appends pollution number
    count += 1  # counter for day
    day.append(count)   # Appends days number
numFile.close() # closes text file

# Prints Table Header
print ("Day\tPollution")

# for loop that prints Day and pollution with appropriate stars
for output in range (len(pollution)):
    print ("%2i%-6s%s (%i)" % (day[output],"",(pollution[output])*"*", pollution[output]))
    
# checks if if 1st number is bigger than 2nd then appends it to lists
if pollution [0] > pollution[1]:
    peaks.append(pollution[0])
    peaksday.append(day[0])

# For loop that checks if a number is bigger than the surrounding numbers
for peak in range(len(day)):
    if peak != 0 and peak < len(pollution)-1:
        if pollution[peak] > pollution[peak-1] and pollution[peak+1]:
            peaks.append(pollution[peak])
            peaksday.append(day[peak])
    if peak == len(pollution)-1:
        if pollution[peak] > pollution[peak-1]:
            peaks.append(pollution[peak])
            peaksday.append(day[peak])            
        
    

# Checks the biggest number in peaks and gets index       
for top in range(len(peaks)):
    for top2 in peaks:
        if top2 > top:
            big = peaks.index(top2)
            
# Adds string for peaks for output
for peaksout in range(len(peaks)):
    peaksoutput += " " +str(peaks[peaksout]) + " " +"(day" + " " + str(peaksday[peaksout]) + ")"+ ","

# Prints the peaks output
print ("peaks are %s with the largest peak on day %i" % (peaksoutput[1:-1], peaksday[big]))