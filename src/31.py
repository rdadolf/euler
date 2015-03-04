#!/usr/bin/env python

import numpy as np
import util

# Strategy:
#   Enforce sorted order in the combinations. I.e.- if you add a certain type
#   of coin, you can only add coins of equal or lesser value later.
#   Then, for a given value, recursively compute the number of combinations
#   for a value minus each denomination, keeping the above rule in mind.

# The rows of the combos array (there are len(denom) of them) reprsent how many
# combinations are possible for a given value using only coins equal to or less
# than the index of the row (for instance, row 2 is using only 1p, 2p, and 5p
# coins).

denoms = [1,2,5,10,20,50,100,200]
combos = np.zeros((len(denoms),201),dtype='i64')
valid = np.zeros((len(denoms),201),dtype='i64')
for (d,_) in enumerate(denoms):
  combos[d,1] = 1
  valid[d,1] = 1

def combinations(d,n):
  if valid[d,n]:
    #print 'c(%d[%d],%d)=%d'%(d,denoms[d],n,combos[d,n])
    return combos[d,n]
  c = 0
  for new_d in xrange(0,d+1):
    new_n = n-denoms[new_d]
    if new_n==0:
      c += 1
    if new_n>0:
      c += combinations(new_d,new_n)
  combos[d,n] = c
  valid[d,n] = 1
  #print 'c(%d[%d],%d)=%d'%(d,denoms[d],n,combos[d,n])
  return c

print combinations( len(denoms)-1, 200 )
