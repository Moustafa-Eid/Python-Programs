word = input("Please Enter String: blah: ")
start = len(word)

for letter in word:
    print("%-5s%s" % (letter, word[start-1]))
    start -= 1