#Created on 27 Feb 2015
from collections import Counter
import sys
sentence = raw_input("Please type your sentence.")
charset = Counter()
count = 0
for char in sentence:#loop through characters in the given sentence
    charset[char] += 1 #increment appropriate space in counter
    char = bin(ord(char)) #change char to the binary version of itself
    if len(char)<9:
        print "",
        for n in range(0,9-len(char)):
            sys.stdout.write('0')#print leading zeros if needed
    print str(char[2:]),#print binary rep of char
    count+=1
    if count >= 8:#skip line every 8 binary numbers
        count = 0
        print ""
print ""
count = 0
charset = charset.items()#convert dictionary to list of lists
charset.sort(key=lambda x: x[1], reverse = True)#sort it by second element reversed
priq = []
for groups in range(0,len(charset)):
    count+=1
    print charset[groups],
    if count>=8:
        print ""
        count = 0

print ""
print "%s bits would be used by ASCII" % (len(sentence)*7)