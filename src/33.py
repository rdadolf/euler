#!/usr/bin/env python

import numpy as np
import util

# ab   a    1<=a<=8
# -- = -    b>=a
# bc   c    a*bc=c*ab

num_prod = 1
den_prod = 1
for a in xrange(1,9): # 9 is not possible
  for b in xrange(a+1,10):
    for c in xrange(0,10):
      ab = a*10+b
      bc = b*10+c
      if a*bc == c*ab:
        #print '%d/%d=%d/%d'%(ab,bc,a,c)
        num_prod *= a
        den_prod *= c

# And now a silly little fraction reducer
S = util.Sieve(100)
num_fact = S.prime_factorization(num_prod)
den_fact = S.prime_factorization(den_prod)
num = num_prod
den = den_prod
for term in num_fact:
  if term in den_fact:
    den_fact.remove(term) # just once
print np.product(den_fact)
