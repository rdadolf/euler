#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

S=util.Sieve(1000000)
P=S.primes()
n_circular = 0
for n in P[P<1000000]: # Only need to consider primes
  digits = str(n)
  n_digits = len(digits)
  digits+=digits # for rotations
  circular = True
  for rot in xrange(0,n_digits):
    m = int(''.join(digits[rot:rot+n_digits]))
    #print m
    if not S.is_prime(m):
      circular = False
      continue
  if circular:
    #print m
    n_circular+=1
print n_circular
