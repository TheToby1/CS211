'''Created on 14 Feb 2015
Grab a stick. Break it in two. Now randomly break another piece in two. Carry out
this process a total of n times.
Write a program that takes n as input and outputs the probability that a triangle can
be formed out of any three of the resulting pieces.

Does not work'''
from random import uniform
import time

def breaker(n, stick1):
    stickdic = []
    for nums in range(0,n):
        stick2 = 0
        while stick2==0:
            stick2 = uniform(0,stick1)
        stick1 = stick1-stick2
        stickdic.append(stick2)
    stickdic.append(stick1)
    return sorted(stickdic)

def trianglecheck(sticks):
    first = 0
    for n in sticks:
        first+=1
        second = first
        for m in sticks[first:]:
            second +=1
            for o in sticks[second:]:
                if n+m>o:
                    return 1
    else:
        return 0

a = time.clock()
times = 10000
count = 0
breaks = 30
stick = 1.0
for nums in range(0,times):
    sticks = breaker(breaks,stick)
    count += trianglecheck(sticks)
print "With %s breaks the chance of making a triangle is %s%%" % (breaks, count/float(times)*100)
print "%s sticks were broken in %sms" % (times, time.clock()-a)
