#Created on 9 Mar 2015
from collections import Counter

with open('encoded.txt','r') as fin:
    filein = fin.read()

charcount = Counter()
count = 0
for chars in filein:
    charcount[chars]+=1
    if (chars != '\n') & (chars !='\r') & (chars != '\xa7') & (chars != 'p'):
        count+=1
print count
print len(filein)
charcount = charcount.items()
dicperc = dict()
for things in charcount:
    dicperc[things[0]] = (things[1]/float(count))*100
del dicperc["\n"]
del dicperc["\r"]
del dicperc["\xa7"]
del dicperc["p"]
dicperc = dicperc.items()
dicperc.sort(key=lambda x: x[1], reverse = True)
print dicperc
with open('percentages.txt','w') as fout:
    for things in dicperc:
        fout.write("%s:%s\n" % (things[0], things[1]))

with open('danish_monograms.txt','r') as fin:
    filein1 = fin.read().splitlines()
print filein1

fdict = dict()
for things in filein1:
    num = things.index(' ')
    fdict[things[0:num]] = int(things[num+1:])
fdict = fdict.items()
fdict.sort(key=lambda x: x[1], reverse = True)
print fdict

bigdic = dict()
for nums in range(0,len(fdict)):
    bigdic[(dicperc[nums])[0]] = (fdict[nums])[0]
print bigdic

newfile = ""
for chars in filein:
    if chars == '\xa7':
        newfile+=' ' 
    elif chars == 'p':
        newfile+='.'
    elif chars == '\n':
        newfile+='\n'
    elif chars == '\r':
        None
    else:
        try:
            newfile += bigdic[chars]
        except:
            newfile += '|'
print newfile

with open('new.txt','w') as fout:
    fout.write(newfile)