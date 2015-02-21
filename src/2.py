#!/usr/bin/env python

import numpy as np

# 4M isn't large. Memoize and brute-force the fibs, then sum every third one

size=500
memo=np.zeros(size,dtype='i64')
memo[0] = 1
memo[1] = 1
for i in range(2,size):
  memo[i] = memo[i-1]+memo[i-2]
  if memo[i]>4000000:
    break
print np.sum(memo[range(2,i,3)])
