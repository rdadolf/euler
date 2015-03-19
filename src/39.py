#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

# Do this backwards: compute the sum of all integer triangles, then increment
# the count of those sums and find the max.
maxP = 1000

# Without loss of generality, a<b<c (just naming)
# A loose upper bound on c is a very oblique triangle
c_limit = maxP//2
# A loose upper bound on b is the hypotenuse (triangle inequality)
b_limit = c_limit-1

# Find all right triangles
scratch = np.zeros((maxP,maxP),dtype='double') # overestimate, don't care
for b in np.arange(1,b_limit):
  for a in np.arange(1,b): # Also so we don't double-count
    scratch[a,b] = a**2 + b**2
exact_roots = np.sqrt(scratch)
approx_roots= np.array(exact_roots,dtype='int64')
right_tri_mask = (exact_roots==approx_roots) & (exact_roots!=0)
assert right_tri_mask[20,48]
assert right_tri_mask[24,45]
assert right_tri_mask[30,40]

# Count them
p = np.zeros(2*(maxP**2),dtype='int64') # overestimate, don't care
for a in np.arange(0,b_limit):
  for b in np.arange(0,b_limit):
    if right_tri_mask[a,b]:
      p[a+b+approx_roots[a,b]] += 1

# Where is the max?
assert p[120]==3
print np.argmax(p)
