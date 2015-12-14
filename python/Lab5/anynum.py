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
Used Ubuntu's dictinoary as it contains more words, also set it up to take in more or less than 9 letters.'''
from collections import Counter

letters = ""
notchar = True

#Takes in user iput for the letters
while notchar:
    notchar = False
    letters = raw_input("Please input a string of letters.\n")
	#Checks if the letter is an apstrophe or any alphabetical char
    for letter in letters:
        if ord(letter) == 39:
            None
        elif ((ord(letter) < 65)) | ((ord(letter) > 90) & (ord(letter) < 97)) | (ord(letter) > 122):
            notchar = True
            print "They were not all letters."

charset = Counter()
#Changes all chars to lower case
letters = letters.lower()
#counts the chars into a counter
for char in letters:
    charset[char] += 1

#takes the dictionary into a list line by line
with open('british-english.txt', 'r') as fin:
    filein = fin.read().splitlines() 
#sorts by length
filein.sort(key = len)
diction = []
#Takes out all words longer than amount of letters given
for words in filein:
    if len(words) <= len(letters):
        diction.append(words.lower())
    else:
        break
#sorts by reverse length
diction.sort(key = len, reverse = True)

good = []
maxim = 1
'''Checker algorithm
compares the word x with the counter of letters given y
if any part of y goes negative it breaks'''
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
		#remembers the longest words
        good.append(words)
print "The longest word has %s letters." % maxim
print good
