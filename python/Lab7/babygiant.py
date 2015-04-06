#Created on 27 Mar 2015
from math import floor,sqrt

def modpower(num1, power, mod):
    if(power==0): return 1
    elif (power%2==0):
        halfpower = modpower(num1, power/2, mod)
        return modmulti(halfpower,halfpower,mod)
    else:
        halfpower = modpower(num1, power/2, mod)
        firstbit = modmulti(halfpower,halfpower,mod)
        return modmulti(firstbit,num1,mod)

def modmulti(num1, num2, mod):
    if(num2==0): return 0
    elif (num2%2==0):
        half=modmulti(num1, num2/2, mod)
        return (half+half)%mod
    else:
        half=modmulti(num1, num2/2, mod)
        return (half+half+num1)%mod
    
def intpow(num1, power):
    if power == 0:
        return 1
    elif power == 1:
        return num1
    elif (power & 1) != 0:
        return num1 * intpow(num1 * num1, power // 2)
    else:
        return intpow(num1 * num1, power // 2)

y = 8414508
g = 2744
p = 24852977
c1 = 15268076
c2 = 743675
'''y = 34109547043
g = 181673
p = 85754635859
c1 = 26398053246
c2 = 72955071594'''

s = int(floor(sqrt(p)))

A = []
B = []

for r in range(0,s):
    value = y * intpow(g,r) % p
    A.append(value)

breakcheck= False
privkey = 0
for t in range(1,s+1):
    value = intpow(g,(t*s)) % p
    B.append(value)
    for r in A:
        if value == r:
            breakcheck = True
            break
    if breakcheck:
        break

x1,x2 =0,0

for r in A:
    for t in B:
        if r == t:
            x1 = A.index(r) 
            x2 = B.index(t)
            break

privkey = ((x2+1)*s - x1) % p
print 'the value of x is %s' % (privkey)



value = modpower(c1,(p-1-privkey),p)
value = modmulti(value, c2, p)
print "The message is: ", value