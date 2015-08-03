def decrement(n): return (n >> 1 << 1) if (n & 1) == 1 else decrement(n >> 1) << 1 | 1
def powertwo(n): return n if (n&decrement(n))==0 else (1<<len(bin(n)))>>2
print "Result: %s" % (powertwo(877))
raw_input()