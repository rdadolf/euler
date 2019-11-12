#!/usr/bin/env python

import math
import itertools
import numpy as np
import util
import sys

def n_choose_r(n,r):
  return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

c = 0
for n in xrange(1,101):
  for r in xrange(1,n):
    if n_choose_r(n,r)>1000000:
      c+=1
print c
