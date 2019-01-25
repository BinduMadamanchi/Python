import math
sentence = input('Enter the sentence in which number of letters, words and digits to be counted:')
countletters = 0
countwords = 0
countdigits = 0
for i in range(len(sentence)):
    if sentence[i].isalpha():
        countletters += 1

for i in range(len(sentence)):
    if sentence[i] == ' ':
        countwords += 1

for i in range(len(sentence)):
    if sentence[i].isnumeric():
        countdigits += 1
print("OUTPUT")
print("Number of letters = %d" %(countletters))
print("Number of words = %d" %(countwords+1))
print("Number of digits = %d" %(countdigits))
