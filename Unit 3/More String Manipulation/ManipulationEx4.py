word = input("Please Enter String: blah: ")
newword = ""
for count in range(len(word)):
    for letter in word:
        if letter == word [count]:
            newword += letter.swapcase()
        else:
            newword += letter
    print (newword)
    newword = ""