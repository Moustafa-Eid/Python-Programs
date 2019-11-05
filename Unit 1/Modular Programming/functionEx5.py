# Name: Moustafa Eid
# Date: February 14th 2017
# Class: ICS3U1-03
# Description: counts capital letters in a inputted sentence

# function for getting all capitals and adding them
def capital (sentence):
    capitals1 = sentence.count ("A")
    capitals2 = sentence.count ("B")
    capitals3 = sentence.count ("C")
    capitals4 = sentence.count ("D")
    capitals5 = sentence.count ("E")
    capitals6 = sentence.count ("F")
    capitals7 = sentence.count ("G")
    capitals8 = sentence.count ("H")
    capitals9 = sentence.count ("I")
    capitals10 = sentence.count ("J")
    capitals11 = sentence.count ("K")
    capitals12 = sentence.count ("L")
    capitals13 = sentence.count ("M")
    capitals14 = sentence.count ("N")
    capitals15 = sentence.count ("O")
    capitals16 = sentence.count ("P")
    capitals17 = sentence.count ("Q")
    capitals18 = sentence.count ("R")
    capitals19 = sentence.count ("S")
    capitals20 = sentence.count ("T")
    capitals21 = sentence.count ("U")
    capitals22 = sentence.count ("V")
    capitals23 = sentence.count ("W")
    capitals24 = sentence.count ("X")
    capitals25 = sentence.count ("Y")
    capitals26 = sentence.count ("Z")
    number = capitals1 + capitals2 + capitals3 + capitals4 + capitals5 + capitals6 + capitals7 + capitals8 + capitals9 + capitals10 + capitals11 + capitals12 + capitals13 + capitals14 + capitals15 + capitals16 + capitals17 + capitals18 + capitals19 + capitals20 + capitals21 + capitals22 + capitals23 + capitals24 + capitals25 + capitals26
    return number

#input a sentence
sentence = input("Please type a sentence: ")
n_capital = capital (sentence)

#print number of capitals
print ("There are %i capital letters in your sentence" % (n_capital))
