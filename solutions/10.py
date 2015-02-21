#!/usr/bin/env python

import numpy as np
import primes

s=primes.Sieve(2000000)
print sum(s.primes())
