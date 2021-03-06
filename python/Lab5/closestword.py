'''Created on 8 Mar 2015 
You have been employed by Channel 4 to write a computer program that
can help the presenters of Countdown.
Contestants must make English words from nine randomly selected
letters using as many of the letters as possible. Judges look up the words
in the dictionary and then make some even better suggestions. You need
to write a computer program to help them with this.
Write a program which takes in a set of nine letters and then prints out
some good solutions for those letters. You will need to load and use the
file dictionary.txt which contains all of the words in the English
language.
This finds the closest word to the given letters
works pretty much the same as as anynum
when comparing counters takes the difference between them, this is the words "score"
The word with the lowest score is closest to the letters given
if a word has 0 missing and 0 spare it is perfect
if it has 0 missing it can be made with the letters but the spare is how many letters were left over'''
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
    diction.append(words.lower())
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
    good[words] = ("Missing:", missing, "Spare:",spare)
good = good.items()             #convert dictionary to list of lists
good.sort(key=lambda x: x[1])   #sort it by second element 
print "The closest 5 words are."
print good[0:5]
print "Time: %s" % (time.clock()-a)
