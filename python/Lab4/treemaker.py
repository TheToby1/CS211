#Created on 28 Feb 2015
from q1_objects import *
import time
code = []
yay = ""

def stepper(localroot, cat): #takes the root of a tree and a character to search for
    global code
    global yay
    if localroot is not None:
        if type(localroot) is leaf: #if a leaf check to see it has the character you want
            if localroot.letter == cat:
                for n in code:
                    yay += str(n) #edits a global variable to equal the answer
        elif isinstance(localroot, node): #otherwise move through the nodes
            code.append(0)#puts a zero on when going left
            stepper(localroot.left, cat)
            code.pop()#takes it off when going back
            code.append(1)#same with 1
            stepper(localroot.right, cat)
            code.pop()
        else: #if the localnode is a tree then change it to be a node
            stepper(localroot.root, cat)
            


def maker(charset):
    a = time.clock()
    priq = []
    for groups in range(0,len(charset)):
        temp = charset[groups]
        priq.append(tree(leaf(temp[0]), temp[1]))
    
    for bums in range(0,len(priq)-1):
        temp = priq.pop()
        temp2 = priq.pop()
        priq.append(tree(node(temp, temp2), temp.frequency+temp2.frequency))
        priq.sort(key=lambda tree: tree.frequency, reverse = True)
    print "Tree made in %s" % (time.clock()-a)
    return priq[0]

def dicmaker(tree1, charset):
    a = time.clock()
    global code
    global yay
    dic = dict()
    for stuff in charset:
        cat = stuff[0]
        code = []
        yay = ""
        stepper(tree1.root, cat)
        dic[cat] = yay
    print "Dictionary made in %s" % (time.clock()-a)
    return dic