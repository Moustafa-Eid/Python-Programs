word = input("Please Enter String: ")
newword = ""
for count in range(len(word)-1):
    if count == 0:
        print(word)
        newword = word[1:3] + word[3] + word[0]
    else:
        newword = newword[1:3] + newword[3] + newword[0]    
    print (newword)
    