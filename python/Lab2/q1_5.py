#Created on 14 Feb 2015
from random import uniform
import time

def breaker(n, stick1):
    stickdic = set()
    while len(stickdic)<=n:
        stickbreak = 0
        while stickbreak == 0:
            stickbreak = uniform(0,stick1)
        stickdic.add(stickbreak)
    stickdic = sorted(list(stickdic))
    count = 1
    newsticks = stickdic
    for nums in range(1,len(stickdic)):
        count+=1
        for times in range(1,count):
            newsticks[nums] -= stickdic[nums-times]
    return sorted(newsticks)

def trianglecheck(sticks):
    first = 0
    while first<len(sticks)-2:
        if sticks[first]+sticks[first+1]>sticks[first+2]:
            return 1
        first+=1
    else:
        return 0

a = time.clock()
times = 1000000
count = 0
breaks = 2
stick = 1.0
for nums in range(0,times):
    sticks = breaker(breaks,stick)
    count += trianglecheck(sticks)
print "With %s breaks the chance of making a triangle is %s%%" % (breaks, count/float(times)*100)
print "%s sticks were broken in %sms" % (times, time.clock()-a)