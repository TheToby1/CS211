# Created on 8 Mar 2015
from collections import Counter
import time

letters = ""
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
    if len(words) <= len(letters):
        diction.append(words)
    else:
        break
diction.sort(key=len,reverse=True)
a = time.clock()

good = []
maxim = 1
for words in diction:
    count = 0
    tmp = charset.copy()
    for char in words:
        if tmp[char] > 0:
            count+=1
            tmp[char]-=1
        else:
            count = -1
            break
    if count >= maxim:
        maxim = count
        good.append(words)
    if maxim>len(words):
        break
print "The longest word has %s letters." % maxim
print good
print "Time: %s" % (time.clock()-a)