#!/usr/bin/env python

import numpy as np
import util

(trinum,delta)=(1,1)
factors = util.factors(trinum)
while len(factors)<500:
  delta+=1
  trinum+=delta
  factors = util.factors(trinum)
print trinum
