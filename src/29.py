#!/usr/bin/env python

import numpy as np
import util


terms = set([])

for a in range(2,100+1):
  for b in range(2,100+1):
    terms.add(a**b)

# We don't actually need to sort them in order to remove duplicates.
print len(terms)
