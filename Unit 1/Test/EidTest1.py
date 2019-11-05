# Name: Moustafa Eid
# Date: March 3rd 2017
# Class: ICS3U1-03
# Description: Display Participants Name and number of minutes he walked/ran

# Calculates time walked/ran in minutes
def timecalc (c, t):
    hours = int(t[0:t.find(':')]) # Seperates hours from input and casts to integer
    minutes = int(t[t.find(':')+1:len(t)]) # Seperates minutes from input and casts to integer
    convhours = hours * c # Converts hours to minutes
    totalcalc = convhours + minutes # Adds up the minutes together
    return totalcalc # Returns the value for the answer in minutes

# Declaring Constant for converting from hours to minutes
CONVERSION_HOURS_TO_MINUTES = 60

# Input gets name and time
name = input("Enter the participant's name (last, first): ")
time = input("Enter the time (hh:mm): ")

# Seperates first and last name
last = (name[0:name.find(',')])
first = (name[name.find(' ')+1:len(name)])

# Assigns variable the value from the function
total = timecalc(CONVERSION_HOURS_TO_MINUTES, time)

# Outputs the final statement with results
print ("%s %s took a total of %i minutes." % (first, last, total))

