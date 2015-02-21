#!/usr/bin/env python

import numpy as np
import util

n = 600851475143

S = util.Sieve()
S.gen(int(np.sqrt(n)))

f = 1
for i in S.primes():
  if n%i==0:
    f = i
print f
