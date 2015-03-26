#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

S=util.Sieve(10000)

# Strategy:
#   pick all primes 

allp=S.primes()
primes = allp[(allp>1000)*(allp<10000)]
primeset = set(primes)

c = 0
for (p,q) in itertools.combinations(primes,2):
  assert q>p
  r = q+(q-p)
  if r not in primeset:
    continue

  pdigits = tuple(sorted(map(int,str(p)))) # slow
  qdigits = tuple(sorted(map(int,str(q)))) # slow
  if pdigits==qdigits:
    rdigits = tuple(sorted(map(int,str(r))))
    if qdigits==rdigits and p!=1487:
      print ''.join(map(str,[p,q,r]))
