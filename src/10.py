#!/usr/bin/env python

import numpy as np
import util

s=util.Sieve(2000000)
print sum(s.primes())
