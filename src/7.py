#!/usr/bin/env python

import numpy as np
import util

s=util.Sieve()
n=1000
s.gen(n)
while len(s.primes())<10001:
  n+=1000
  s.gen(n)

print s.primes()[10000]
