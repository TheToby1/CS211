#Created on 8 Mar 2015
from collections import Counter

letters = ""
notchar = True
while notchar:
    notchar = False
    letters = raw_input("Please input a string of letters.\n")
    for letter in letters:
        if ord(letter) == 39:
            None
        elif ((ord(letter) < 65)) | ((ord(letter) > 90) & (ord(letter) < 97)) | (ord(letter) > 122):
            notchar = True
            print "They were not all letters."
charset = Counter()
letters = letters.lower()
for char in letters:
    charset[char] += 1
    
with open('british-english.txt', 'r') as fin:
    filein = fin.read().splitlines() 
filein.sort(key = len)
diction = []
for words in filein:
    if len(words) <= len(letters):
        diction.append(words)
    else:
        break
diction.sort(key = len, reverse = True)

good = []
maxim = 1
for words in diction:
    count = 0
    tmp = charset.copy()
    if maxim>len(words):
        break
    for char in words:
        if tmp[char] > 0:
            count+=1
            tmp[char]-=1
        else:
            count = 0
            break
    if count >= maxim:
        maxim = count
        good.append(words)
print "The longest word has %s letters." % maxim
print good