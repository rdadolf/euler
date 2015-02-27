#!/usr/bin/env python

import numpy as np
import util

tri=[
[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20, 4,82,47,65],
[19, 1,23,75, 3,34],
[88, 2,77,73, 7,63,67],
[99,65, 4,28, 6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,50,27,29,48],
[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
[04,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23]
]

dim = (len(tri), len(tri[-1]))
A = np.zeros(dim,dtype='i64')
for (r,L) in enumerate(tri):
  for (c,v) in enumerate(L):
    A[r,c]=v

# This is a simple dynamic programming problem. For each position, we just
# compute the maximum sum of a path that ends there. Can't do it greedily
# because a path that starts bad could end well.
(nR,nC) = dim
maxsum = np.zeros(dim,dtype='i64')
sum_L = np.zeros(nC,dtype='i64')
sum_R = np.zeros(nC,dtype='i64')
maxsum[0,:] = A[0,:]

for r in xrange(1,nR):
  sum_L[0:nC-1] = A[r,0:nC-1] + maxsum[r-1,0:nC-1]
  sum_R[1:nC] = A[r,1:nC] + maxsum[r-1,0:nC-1]
  maxsum[r,:] = np.maximum(sum_L,sum_R)

print np.max(maxsum[nR-1,:])
