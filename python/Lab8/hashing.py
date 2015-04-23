#Created on 21 Apr 2015

def hashkey(key):
    key = ~key + (key << 15)
    key = key ^ (key >> 12)
    key = key + (key << 2)
    key = key ^ (key >> 4)
    key = key * 2057
    key = key ^ (key >> 16)
    return key
def linearprobing():
    global filein
    global hashtable
    #times = Counter()
    collisions = 0
    for words in filein:
        placed = False
        maxi = 0
        for nums in range(0,len(words)):
            maxi += (ord(words[nums])-96)*(27**nums)
        index = hashkey(maxi)%size
        #times[index] +=1
        while not placed:
            if index >= len(hashtable):
                index-=len(hashtable)
                
            if hashtable[index] == None:
                hashtable[index] = words
                placed = True
            elif hashtable[index] == 666:
                hashtable[index] = words
                placed = True
            else:
                index+=1
                collisions+=1
    print "Number of collisions:", collisions
def searchlinear(word):
    global hashtable
    probes = 1
    maxi = 0
    found = False
    for nums in range(0,len(word)):
            maxi += (ord(word[nums])-96)*(27**nums)
    index = hashkey(maxi)%size
    while not found:
        if index >= len(hashtable):
                index-=len(hashtable)
                
        if hashtable[index]==None:
            print "NOT IN HASHTABLE."
            found = True
        elif hashtable[index]==word:
            print "The word %s was found in slot %s of the hashtable." % (word,index)
            found = True
        else:
            index+=1
            probes+=1
    print "Number of hash table probes: ", probes
def quadraticprobing():
    global filein
    global hashtable
    #times = Counter()
    collisions = 0
    for words in filein:
        count = 1
        placed = False
        maxi = 0
        for nums in range(0,len(words)):
            maxi += (ord(words[nums])-96)*(27**nums)
        index = hashkey(maxi)%size
        #times[index] +=1
        while not placed:
            if index >= len(hashtable):
                index-=len(hashtable)
                
            if hashtable[index] == None:
                hashtable[index] = words
                placed = True
            elif hashtable[index] == 666:
                hashtable[index] = words
                placed = True
            else:
                index+=(count**2)
                count+=1
                collisions+=1
    print "Number of collisions:", collisions
def searchquadratic(word):
    global hashtable
    probes = 1
    maxi = 0
    found = False
    for nums in range(0,len(word)):
            maxi += (ord(word[nums])-96)*(27**nums)
    index = hashkey(maxi)%size
    while not found:
        if index >= len(hashtable):
                index-=len(hashtable)
                
        if hashtable[index]==None:
            print "NOT IN HASHTABLE."
            found = True
        elif hashtable[index]==word:
            print "The word %s was found in slot %s of the hashtable." % (word,index)
            found = True
        else:
            index+=probes**2
            probes+=1
    print "Number of hash table probes: ", probes
def doublehash():
    global filein
    global hashtable
    global jumpsize
    #times = Counter()
    collisions = 0
    for words in filein:
        sechash = 0
        placed = False
        maxi = 0
        mini = 0
        for nums in range(0,len(words)):
            maxi += (ord(words[nums])-96)*(27**nums)
            mini += (ord(words[nums])-96)*(128**nums)
        index = hashkey(maxi)%size
        sechash = jumpsize - (hashkey(mini)%jumpsize)
        #times[index] +=1
        while not placed:
            if index >= len(hashtable):
                index-=len(hashtable)
                
            if hashtable[index] == None:
                hashtable[index] = words
                placed = True
            elif hashtable[index] == 666:
                hashtable[index] = words
                placed = True
            else:
                index+=sechash
                collisions+=1
    print "Number of collisions:", collisions
def main():
    searching = False
    probetype = raw_input("Which type of open addressing would you like to use?\n1) Linear Probing\n2) Quadratic Probing\n3) Double Hashing\n")
    if probetype == '1':
        linearprobing()
        searching = True
    elif probetype == '2':
        quadraticprobing()
        searching = True
    elif probetype == '3':
        doublehash()
        searching = True
    while searching:
        search = raw_input("Press 1 if you would like to search for a word?\n")
        if not search == '1':
            searching = False
        elif probetype == '1':
            word = raw_input("What word would you like to search for?\n")
            searchlinear(word.lower())
        elif probetype == '2':
            word = raw_input("What word would you like to search for?\n")
            searchquadratic(word.lower())
#400009          
size = 238151
#76403
jumpsize = 1249
hashtable = [None] * size

with open("dictionary.txt", "r") as fin:
    filein = fin.read().splitlines()
    
main()
