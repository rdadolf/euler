#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

#(t,T)=(2,3)
#(p,P)=(2,5)
#(h,H)=(2,6)
(t,T)=(285,40755)
(p,P)=(165,40755)
(h,H)=(143,40755)
T += t+1
t += 1

while T!=P or P!=H or T!=H:
  if T<=P and T<=H:
    T += t+1
    t += 1
  elif P<=T and P<=H:
    P += 3*p+1
    p += 1
  elif H<=T and H<=P:
    H += 4*h+1
    h += 1
  else:
    assert 0, str(((h,H),(t,T),(p,P)))

assert T==P==H
print T
