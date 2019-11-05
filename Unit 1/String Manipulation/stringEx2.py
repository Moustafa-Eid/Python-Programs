# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: Prints extention of file

# input file name
filename = input ("Please Enter The File Name: ")

#printing extension
print (filename[filename.find('.'):len(filename)])