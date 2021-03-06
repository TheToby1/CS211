'''Created on 14 Feb 2015
Grab a stick. Break it in two. Now randomly break another piece in two. Carry out
this process a total of n times.
Write a program that takes n as input and outputs the probability that a triangle can
be formed out of any three of the resulting pieces.

Does not work'''
from random import uniform
import time

def breaker(n):
    stick1 = 1.0
    stickdic = set()
    for nums in range(0,n):
        stick2 = 0
        while stick2==0:
            stick2 = uniform(0,stick1)
        stick1-=stick2
        stickdic.add(stick2)
    stickdic.add(stick1)
    return stickdic

a = time.clock()
times = 100000
count = 0
breaks = 2
for nums in range(0,times):
    sticks = breaker(breaks)
    for n in sticks:
        if n > 0.5:
            break
    else:
        count+=1
print "With %s breaks the chance of making a triangle is %s%%" % (breaks, count/float(times)*100)
print "%s sticks were broken in %sms" % (times, time.clock()-a)
