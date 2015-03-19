#!/usr/bin/env python

import math
import itertools
import numpy as np
import util


# Strategy: start with a low difference, and find a J&K that satisfy it.
def w0():
  n=np.arange(0,10000,dtype='int64') # should be sufficient
  pents = n*(3*n-1)/2
  pcheck=set(pents)
  for D in pents[1:]: # will short-circuit
    for J in pents[1:]:
      K=J+D
      if K in pcheck and K+J in pcheck:
        return D

#import timeit
#print 'Way 0:',timeit.timeit(w0,number=1)
print w0()
