#Created on 8 Mar 2015
from collections import Counter
import time
letters = ""
alpha = True
while not letters.isalpha():
    letters = raw_input("Please input a string of letters.\n")
charset = Counter()
letters = letters.lower()
for char in letters:
    charset[char] += 1

with open('british-english.txt', 'r') as fin:
    filein = fin.read().splitlines() 
filein.sort(key = len)
diction = []
for words in filein:
    if len(words) > len(letters): break
    diction.append(words)
diction.sort(key = len, reverse = True)
a = time.clock()

good = dict()
for words in diction:
    tmp = charset.copy()
    spare = 0
    missing = 0
    wordset = Counter()
    for char in words:
        wordset[char] += 1
    tmp.subtract(wordset)
    tmp = tmp.items()
    for stuff in tmp:
        if stuff[1]<0: missing -= stuff[1]
        else: spare += stuff[1]
    good[words] = ("Spare:",spare, "Missing:", missing)
good = good.items()             #convert dictionary to list of lists
good.sort(key=lambda x: x[1])   #sort it by second element 
print "The closest 5 words are."
print good[0:5]
print "Time: %s" % (time.clock()-a)
