#!/usr/bin/env python

import numpy as np
import util

# Strategy:
#   Implement long division and record all the divisor/dividend pairs.
#   If we ever have the same divisor and dividend, then it's a cycle.
#   Then compute the repeated segement from the index of the match.

max_cycle = 0
max_divisor = 1
for divisor in xrange(2,1000):
  states = []
  dividend = 10
  while( (dividend,divisor) not in states ):
    states.append( (dividend,divisor) )
    remainder = dividend % divisor
    dividend = remainder*10
  if dividend==0: # Not repeating
    #print divisor,'Not repeating'
    continue
  cycle = len(states)-states.index((dividend,divisor))
  #print divisor,cycle
  if( cycle>max_cycle ):
    max_cycle = cycle
    max_divisor = divisor
print max_divisor
