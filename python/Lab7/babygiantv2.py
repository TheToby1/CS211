#Created on 27 Mar 2015
from math import ceil,sqrt
import time

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x,
def modinv(a, m):
    gcd, x = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

a = time.time()

'''y = 8414508
g = 2744
p = 24852977
c1 = 15268076
c2 = 743675
'''
y = 34109547043
g = 181673
p = 85754635859
c1 = 26398053246
c2 = 72955071594


m = int(ceil(sqrt(p)))

A = [1]
B = [y]
value = g % p
A.append(value)
for r in range(1,m):
    value = (value*g) % p
    if value == 1: break;
    A.append(value)

value1 = modinv(g, p)
value1 = pow(value1, m, p)


value = (value1 * y) % p
for t in range(1,m):
    B.append(value)
    value = (value * value1) % p
    
C = list(set(A)&set(B))
privkey = B.index(C[0])*m+A.index(C[0])

print 'the value of x is %s' % (privkey)

value = pow(c1,(p-1-privkey),p)
value = (value * c2) % p
print "The message is:", value
print "run in %s " % (time.time()-a)