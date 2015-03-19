#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

def w1():
  s = 0
  for digits in itertools.permutations('0123456789'):
    d = ''.join(digits)
    if int(d[1:4])%2==0 and \
       int(d[2:5])%3==0 and \
       int(d[3:6])%5==0 and \
       int(d[4:7])%7==0 and \
       int(d[5:8])%11==0 and \
       int(d[6:9])%13==0 and \
       int(d[7:10])%17==0:
      s += int(d)
  return s

def w2():
  s = 0
  for d in itertools.permutations(map(int,list('0123456789'))):
    if (d[5]==5 or d[5]==0) and \
       (d[3])%2==0 and \
       (100*d[2]+10*d[3]+d[4])%3==0 and \
       (100*d[4]+10*d[5]+d[6])%7==0 and \
       (100*d[5]+10*d[6]+d[7])%11==0 and \
       (100*d[6]+10*d[7]+d[8])%13==0 and \
       (100*d[7]+10*d[8]+d[9])%17==0:
      #print int(''.join(map(str,d)))
      s += int(''.join(map(str,d)))
  assert s==16695334890
  return s

# d_6 must be 0 or 5 (d456%5==0)
# d_6 cannot be 0 (d678%11==0, and any 2-digit number must have repeated digits)
def w3():
  s = 0
  for d in itertools.permutations([0,1,2,3,4,6,7,8,9]): # d_6 is 5
    if (not d[3]&1) and \
       (100*d[2]+10*d[3]+d[4])%3==0 and \
       (100*d[4]+50     +d[5])%7==0 and \
       (500     +10*d[5]+d[6])%11==0 and \
       (100*d[5]+10*d[6]+d[7])%13==0 and \
       (100*d[6]+10*d[7]+d[8])%17==0:
      #print int(''.join(map(str,d[0:5])+['5']+map(str,d[5:])))
      s += int(''.join(map(str,d[0:5])+['5']+map(str,d[5:])))
  #print s
  assert s==16695334890
  return s

#import timeit
#print 'Way 1',timeit.timeit(w1,number=1)
#print 'Way 2',timeit.timeit(w2,number=1)
#print 'Way 3',timeit.timeit(w3,number=1)

print w3()
