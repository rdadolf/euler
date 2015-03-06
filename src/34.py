#!/usr/bin/env python

import numpy as np
import util
import math
import itertools

# Strategy:
#   Sums are commutative, and we know that we can only have up to 6-ish digit
#     numbers. So let's compute all of the sums and store them in a set.
#   Curious numbers are recursive. That is, if you take any one, sum the 
#     factorials of their digits, you get itself---which you can then take
#     the sum of the factorials of its digits to get itself again.
#   This is useful because it means that a number is curious if and only if
#     it is in our set of sums.
#   So we can just iterate over the set our sums and check whether each is
#     curious.
#   Why is this good? Because the size of our set is very small.

# First, establish a loose upper bound in digits
max_d=1
while( max_d*math.factorial(9) > (10**max_d)-1 ):
  max_d+=1
#print max_d

# Some helpers
fact = np.zeros(10,dtype='i64')
for i in range(0,10):
  fact[i] = math.factorial(i)
def fact_help(n):
  return fact[int(n)]

digits=[0,1,2,3,4,5,6,7,8,9]
fact_sums = set([])
for d in xrange(2,max_d+1):
  # Technically, this generates numbers that can look like this: 0001234
  # But they will fail the second filter for curiousness, so it doesn't matter.
  # Also, the sum 4321000 would've existed anyways, so it doesn't matter.
  fact_sums |= set([ sum(map(math.factorial,order)) for order in itertools.combinations_with_replacement(digits,d) ])
#print len(fact_sums)

s=0
for n in fact_sums:
  if n>9 and n==sum(map(fact_help,str(n))):
    #print n
    s+=n
print s
