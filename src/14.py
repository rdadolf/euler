#!/usr/bin/env python

import numpy as np
import util

maxlen=1
maxi=1
# must be odd (to exceed 1M in chain--even numbers start at a disadvantage)
# probably over .5M (not guaranteed)
for init in xrange(500001,1000000,2):
  len=1
  i=init
  while i!=1:
    len+=1
    if i%2==0:
      i=i/2
    else:
      i=3*i+1
  if len>maxlen:
    maxlen=len
    maxi=init
print maxi

