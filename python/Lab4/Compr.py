#Created on 27 Feb 2015
import cStringIO
import cPickle
import time
'''takes in a dictionary of character to huffman conversions
The sentence to be stored
and the frequency of all letters to be serialized
'''
def comp(dic, sentence, charset):
    a = time.clock()
    b = time.clock()
    saved=""
    saver = ""
    bits = 0
    #adds the huffman for each character to the answer
    for car in sentence:
        saved += dic[car]
    #ads trailing 0's for de-compressor
    while(len(saved)%8!=0):
        saved += '0'
        bits += 1
    print "Converted to huffman in %s" % (time.clock()-b)
    b = time.clock()
	#serializes charset
    pickled = cStringIO.StringIO()
    pickled.write(cPickle.dumps(charset, cPickle.HIGHEST_PROTOCOL))
    length = len(pickled.getvalue())
    print "Pickled in %s" % (time.clock()-b)
    
	#open the file and write all information in binary by converting every 8 bits to a character
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
