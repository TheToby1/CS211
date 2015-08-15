'''Created on 27 Mar 2015
Write a program that takes encoded.txt as input and outputs the
European language that it is in.Come up with some metric for quantifying
how good the fit is.'''
from collections import Counter
import codecs

#takes in the encoded file
with codecs.open ('encoded-new.txt', 'rb', encoding='utf-8') as filein:
    temp = (filein.read())

#counts the frequency of letters into percentages
def countem(temp):
    charcount = Counter()
    count = 0
    for char in temp:
        if ord(char)>31:
            charcount[char]+=1
            count+=1
    charcount = charcount.items()
    end = []
    for things in charcount:
        end.append((things[0],(things[1]/(float(count)))*100))
    end.sort(key=lambda x: x[1], reverse = True)
    return end

encoded = countem(temp)
encoded.pop(0)
print "Encoded"
print encoded

#takes in the langauge files
def experc(temp):
    ntemp = []
    for stuff in temp:
        place = stuff.index(':')
        ntemp.append((stuff[0:place],float(stuff[place+1:])))
    ntemp.sort(key=lambda x: x[1], reverse = True)
    return ntemp

#calculates the difference between two counted languages and prints it
def diffcalc(encoded, temp):
    total = 0
    for nums in range(0,len(temp)):
        test = (temp[nums])[1]-(encoded[nums])[1]
        
        if test>0:
            total+=test
        else:
            total-=test
    print "Diff %s" % (total)
    
#all the languages opened and compared to the encoded file
with open('danish.txt', 'r') as filein:
    temp = filein.read().splitlines()
danish = experc(temp)
print "Danish"
print danish
diffcalc(encoded,danish)

with open('finnish.txt', 'r') as filein:
    temp = filein.read().splitlines()
finnish = experc(temp)
print "Finnish"
print finnish
diffcalc(encoded,finnish)

with open('english.txt', 'r') as filein:
    temp = filein.read().splitlines()
english = experc(temp)
print "English"
print english
diffcalc(encoded,english)

with open('french.txt', 'r') as filein:
    temp = filein.read().splitlines()
french = experc(temp)
print "French"
print french
diffcalc(encoded,french)

with open('german.txt', 'r') as filein:
    temp = filein.read().splitlines()
german = experc(temp)
print "German"
print german
diffcalc(encoded,german)
