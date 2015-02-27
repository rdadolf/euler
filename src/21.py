#!/usr/bin/env python

import numpy as np
import util

sum_divs = np.zeros(10000,dtype='i64')

# Compute all divisor sums
for i in xrange(1,10000):
  sum_divs[i] = sum(util.factors(i))-i

# Count all amicable numbers
sum = 0
for a in xrange(1,10000):
  b = sum_divs[a]
  if b<10000 and a==sum_divs[b]: # if it's not, they're not
    if a<b: # don't double-count pairs
      sum += a+b

print sum
