from random import shuffle
import time
a = time.clock()
n = range(1,46)
times =100000
count = 0
for nums in range(0,times):
    shuffle(n)
    lotto = n[0:6]
    lotto.sort()
    for i in range(0,5):
        if lotto[i] == lotto[i+1]-1:
            count+=1
            break

print (times-count)/float(times)
print time.clock()-a
raw_input()