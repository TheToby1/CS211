'''Created on 17 Feb 2015
Write a Java program which takes in a line from the user (using Scanner)
and then outputs
i) The sentence in ASCII
ii) Each letter in the sentence and its frequency 
First version, fits lab, bad presentation
'''
from collections import Counter
import sys
sentence = raw_input("Please type your sentence.")
charset = Counter()
for char in sentence:
    charset[char] += 1
    char = bin(ord(char))
    if len(char)<9:
        print "",
        for n in range(0,9-len(char)):
            sys.stdout.write('0')
    print str(char[2:]),
print " "
print charset
