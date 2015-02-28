#!/usr/bin/env python

import numpy as np
import util
import itertools

# First, compute all abundant sums
raw_abundants = np.zeros(28123,dtype='i64')
i=0
for n in xrange(1,28123):
  s = sum(util.factors(n))-n
  if s>n:
    raw_abundants[i] = n
    i+=1
ab_sums = raw_abundants[np.nonzero(raw_abundants)]

# Now sieve out all sums
sieve = np.zeros(ab_sums[-1]*2+1,dtype='i64') + 1
sieve[0] = 0

for (a,b) in itertools.combinations_with_replacement(ab_sums,2):
  sieve[a+b] = 0

not_sums = np.where(sieve[0:28123]>0)[0]

print np.sum(not_sums)
