#!/usr/bin/env python

import numpy as np
import util

S = util.Sieve(1000)
B = S.primes()[S.primes()<1000]
# (n^2 + an + b) for n=0 to ?
# @n=0, b must be prime, so only select prime b
max_n = 0
max_ab = (0,0)
for a in xrange(-999,1000):
  for b in B:
    n=1
    x = n*n + a*n + b
    while( x>0 and S.is_prime(x) ):
      n+=1
      x = n*n + a*n + b
    if n>max_n:
      max_n = n
      max_ab = (a,b)
      #print max_n, max_ab
#print max_n, max_ab
print max_ab[0]*max_ab[1]
