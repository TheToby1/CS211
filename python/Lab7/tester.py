#Created on 4 Apr 2015
def modmulti(num1, num2, mod):
    if(num2==0): return 0
    elif (num2%2==0):
        half=modmulti(num1, num2/2, mod)
        return (half+half)%mod
    else:
        half=modmulti(num1, num2/2, mod)
        return (half+half+num1)%mod  
    
    
import time
a = time.clock()
for n in range(10):
    10000000000000*1000000000000%10000000000
print "run in %s " % (time.clock()-a)
a = time.clock()
for n in range(10):
    modmulti(10000000000000,1000000000000,10000000000)
print "run in %s " % (time.clock()-a)