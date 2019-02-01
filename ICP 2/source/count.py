fileName= "hello.txt"
infile= open(fileName,'r')
line = infile.readline()
print(line)
while line != "":
    countletters = 0
    countwords = 0
    for i in range(len(line)):
        if line[i].isalpha():
            countletters += 1
        if line[i] == " ":
            countwords += 1
    print("Number of letters : %d" % (countletters))
    print("words: %d" % (countwords + 1))
    line = infile.readline()
    print(line)






