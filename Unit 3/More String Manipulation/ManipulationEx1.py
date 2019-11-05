word = input("Please Enter String: blah: ")

for letter in word:
    print("%-5s%i" % (letter, len(word)))