#Created on 27 Feb 2015
import cStringIO
import cPickle
import time

def comp(dick, sentence, charset):
    a = time.clock()
    b = time.clock()
    saved=""
    saver = ""
    bits = 0
    for car in sentence:
        saved += dick[car]
    while(len(saved)%8!=0):
        saved += '0'
        bits += 1
    print "Converted to huffman in %s" % (time.clock()-b)
    b = time.clock()
    pickled = cStringIO.StringIO()
    pickled.write(cPickle.dumps(charset, cPickle.HIGHEST_PROTOCOL))
    length = len(pickled.getvalue())
    print "Pickled in %s" % (time.clock()-b)
    
    n = 8
    fout = open('out.bin', 'wb')
    length = format(length, '032b')
    saverbins = [length[i:i + n] for i in range(0, len(length), n)]
    saverints = []
    for nums in saverbins:
        saverints.append(int(nums, 2))
    for nums in saverints:
        saver += chr(nums)
    saver += pickled.getvalue()
    saver += chr(bits)
    b = time.clock()
    saverbins = [saved[i:i + n] for i in range(0, len(saved), n)]
    saverints = []
    for nums in saverbins:
        saverints.append(int(nums, 2))
    for nums in saverints:
        saver += chr(nums)
    print "Binary converted to askii in %s" % (time.clock()-b)
    fout.write(saver)
    fout.close()
    print "Compressed in %s" % (time.clock()-a)