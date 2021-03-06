'''Write a program that takes in an int and prints out the next power of
2 (e.g. 5 -> 8, 4 -> 4, 17 -> 32, 1 -> 1, 61 -> 64). Don’t use any loops.
Don’t use any arithmetic. Only use bit-shifting. '''
def decrement(n): return (n >> 1 << 1) if (n & 1) == 1 else decrement(n >> 1) << 1 | 1
def powertwo(n): return n if (n&decrement(n))==0 else (1<<len(bin(n)))>>2
print "Result: %s" % (powertwo(2))
