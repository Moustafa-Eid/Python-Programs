# Input file name
file = input("Please enter the file name: ")

# Finds the Extension
extension = file[file.find('.'):len(file)]

#if statements to define popular extensions and identify
if ".doc" == extension:
    print ("\""+file+"\" is a word document")
elif ".mp3" == extension:
    print ("\""+file+"\" is a sound file")
elif ".avi" == extension:
    print ("\""+file+"\" is a video file")
elif ".png" == extension:
    print ("\""+file+"\" is a image file")
elif ".py" == extension:
    print ("\""+file+"\" is a python file")
else:
    print ("Unknown File")

