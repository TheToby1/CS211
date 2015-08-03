from random import shuffle
import time
'''Write a Java program that uses a Monte Carlo algorithm to calculate the
probability that next week's lottery draw won't have any consecutive
pairs of numbers (eg 8 and 9 or 22 and 23). Six numbers are drawn
from 1 to 45.'''
a = time.clock()
n = range(1,46)
times =1000000
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
