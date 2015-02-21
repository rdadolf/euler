#!/usr/bin/env python

import numpy as np
import util

S=util.Sieve(100)
s = set()
pfs = map(S.prime_factorization,range(2,21))
for pf in pfs:
  s |= set(pf)
primes = sorted(list(s))
counts = [max(map(lambda x:x.count(p), pfs)) for p in primes]
#print primes
#print counts
prod = reduce(lambda x,y:x*y, [p**c for (p,c) in zip(primes, counts)])
print prod
