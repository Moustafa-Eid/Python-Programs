# Name: Moustafa Eid
# Date: March 3rd 2017
# Class: ICS3U1-03
# Description: Display Participants Name and number of minutes he walked/ran

# Declaring Constant for converting from hours to minutes
CONVERSION_HOURS_TO_MINUTES = 60

# Input gets name ant time
name = input("Enter the participant's name (last, first): ")
time = input("Enter the time (hh:mm): ")

# Seperates first and last name
last = (name[0:name.find(',')])
first = (name[name.find(' ')+1:len(name)])

# Seperates minutes and hours
hours = int(time[0:time.find(':')])
minutes = int(time[time.find(':')+1:len(time)])

# Calculates hours in to minutes then adds them together
convhours = hours * CONVERSION_HOURS_TO_MINUTES # Used to convert hours to minutes
total = convhours + minutes

# Outputs the final statement with results
print ("%s %s took a total of %i minutes." % (first, last, total))

