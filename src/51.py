#!/usr/bin/env python

import math
import itertools
import numpy as np
import util
import sys

S = util.Sieve(1000000)

maskset = dict()
max_len=7
for digitstr in [bin(n)[2:] for n in xrange( 1, (2**max_len)-1 )]:
  multiplier = int(digitstr)
  masks = [10**i*d for (i,d) in enumerate(reversed(map(int,digitstr))) if d]
  maskset[multiplier] = masks
#print len(maskset)

for p in S.primes():
  for (mult,masks) in filter(lambda t:t[0]<p, maskset.items()):
    base = p - sum([p//m%10*m for m in masks])
    if p//mult>9: # don't start with 0
      R = range(0,10)
    else:
      R = range(1,10)
    c = len(filter(S.is_prime, [base + d*mult for d in R]))
    if c>7:
      #print p,c,mult
      print filter(S.is_prime, [base + d*mult for d in R])[0]
      sys.exit(0)
