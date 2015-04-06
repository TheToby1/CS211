#Created on 14 Feb 2015
from random import uniform
import time

def breaker(n, stick1):
    stickdick = []
    for nums in range(0,n):
        stick2 = 0
        while stick2==0:
            stick2 = uniform(0,stick1)
        stick1 = stick1-stick2
        stickdick.append(stick2)
    stickdick.append(stick1)
    return sorted(stickdick, reverse = True)

a = time.clock()
times = 1000000
count = 0
breaks = 2
stick = 1.0
for nums in range(0,times):
    valid = 0
    sticktest=stick
    diviser = stick/2.0
    sticks = breaker(breaks,stick)
    for n in sticks:
        if n > diviser:
            sticktest = sticktest-n
            valid+=1
            diviser = sticktest/2.0
    if valid < breaks-1:
        count+=1
print "With %s breaks the chance of making a triangle is %s%%" % (breaks, count/float(times)*100)
print "%s sticks were broken in %sms" % (times, time.clock()-a)