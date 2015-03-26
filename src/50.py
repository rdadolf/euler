#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

S=util.Sieve(1000000)

# sequence must be longer than 21, so max prime can't be more than 1M/21
primes = S.primes()[S.primes()<1000000/21]
#print len(primes)

max_c = 21
max_p = 953

for (i,p) in enumerate(primes):
  for j in xrange(0,i-max_c):
    acc = np.sum(primes[j:i+1])
    if acc>1000000:
      break # larger sums in this loop will always be larger than 1M
    c = i+1-j
    if S.is_prime(acc) and c>max_c:
      #print c,acc
      max_c = c
      max_p = acc

print max_p
