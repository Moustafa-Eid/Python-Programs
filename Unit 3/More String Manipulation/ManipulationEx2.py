word = input("Please Enter String: blah: ")
start = len(word)

for letter in word:
    print("%-5s%i" % (word[start-1], len(word)))
    start -= 1