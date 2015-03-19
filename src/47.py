#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

S=util.Sieve(10000)
P=S.primes()[0:200] # The first 200 primes should be enough

def w0():
  i=2
  consecutive=0
  lim=3
  while True:
    pfs = set()
    for p in P:
      if i%p==0:
        pfs.add(p)
    if len(pfs)==lim+1:
      consecutive+=1
      if consecutive>lim:
        #print 'winners:'
        #print [(n,S.prime_factorization(n)) for n in xrange(i-consecutive+1,i+1)]
        return i-consecutive+1
    else:
      consecutive=0
    i=i+1

print w0()
