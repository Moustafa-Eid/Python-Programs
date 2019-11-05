numFile = open("in.txt", "r")
nums = []
while True:
    num = numFile.readline()
    if num == "":
        break
    nums.append(int(num[:-1]))
numFile.close()

for double in nums:
    print("Number = %i, Double = %i" % (double, double*2))

