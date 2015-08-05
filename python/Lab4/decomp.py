#Created on 27 Feb 2015
import binascii
import cPickle
from treemaker import maker
from q1_objects import *
import time

b = time.clock()
a = time.clock()
#opens the compressed file
with open('out.bin', 'rb') as fin:
    doc = fin.read()
length = 0
lstring = ""
#gets the length of the compressed file stored in first 4 characters and convertsit to an int
for num in doc[0:4]:
    lstring += num
length = int(binascii.hexlify(lstring), 16) + 4
doc1 = doc[4:length]

#unloads the pickled charset
charset = cPickle.loads(doc1)
print "Dictionary unpickled in %s" % (time.clock()-a)

#cuts trailing 0's off the file
doc1 = doc[length:]
#rebuilds the tree
tree1 = maker(charset)

#de-compresses chars into binary string
a = time.clock()
length = int(binascii.hexlify(doc1[0]), 16)
doc1 = doc1[1:]
lstring = ""
for weebyte in doc1:
    lstring += format(ord(weebyte), '08b')
for times in range(0,length):
    lstring = lstring[:-1]
print "Binary string uncompressed in %s" % (time.clock()-a)
a = time.clock()
answer = ""
current = tree1.root

#steps through binary string adding the characters to the answer.
for weebits in lstring:
    if weebits == '0':
        current = current.left
    else:
        current = current.right
    
    if isinstance(current, tree):
        current = current.root
    
    if type(current) is leaf:
        answer += current.letter
        current = tree1.root
#answer is the same as original file
print "Binary string converted in %s" % (time.clock()-a)
with open('bibleanswer.txt', 'wb') as fout:
    fout.write(answer)
print "All done in %s" % (time.clock()-b)
