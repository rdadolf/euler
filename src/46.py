#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

S=util.Sieve(100000) # may need to allocate more 
P=S.primes() # does not grow dynamically

def w0():
  (sq_i,pr_i)=(1,0)
  (sq,pr)=(2*sq_i*sq_i, P[pr_i])
  
  limit = max(sq,pr)
  
  ocomps=np.zeros(100000,dtype='int64')+1 # may need to alloc more space
  ocomps[1]=0
  ocomps[0:100000:2]=0
  ocomps[P]=0

  while True:
    #if limit>5770:
    if sq>pr: # square-limited, bump the prime
      pr_i += 1
      pr = P[pr_i]
      # sieve with the new prime
      for s_i in xrange(1,sq_i+1):
        ocomps[2*s_i*s_i + pr] = 0
    else: # prime-limited, bump the square
      sq_i += 1
      sq = 2*sq_i*sq_i
      # sieve with the new square
      for p_i in xrange(0,pr_i+1):
        ocomps[sq + P[p_i]] = 0
    # bump the limit and check for new composites in between
    newlim = min(sq,pr)
    #print (sq,pr,limit,newlim)
    #print max(0,limit-5),ocomps[max(0,limit-5):limit],'|',ocomps[limit:newlim],':',ocomps[newlim:newlim+5],newlim+5
    comps = np.nonzero(ocomps[limit:newlim])[0]
    #print 'nonzeros:',comps
    if comps.shape[0]>0:
      return limit+comps[0]
    limit = newlim

print w0()  
