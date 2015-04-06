# Created on 24 Feb 2015
from collections import Counter #used to count chars
from treemaker import * #all my objects for the binary tree
from Compr import comp
import time

a = time.clock()
with open('bible.txt','rb') as f: #opens the file in read mode
    sentence = f.read()
charset = Counter()
count = 0
for char in sentence:#loop through characters in the given sentence
    charset[char] += 1 #increment appropriate space in counter

charset = charset.items()#convert dictionary to list of lists
charset.sort(key=lambda x: x[1], reverse = True)#sort it by second element reversed

tree1 = maker(charset)
dick = dicmaker(tree1, charset)

comp(dick, sentence, charset)
print "All done in %s" % (time.clock()-a)