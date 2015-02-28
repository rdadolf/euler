#!/usr/bin/env python

import numpy as np
import util

lim = 10**(1000-1)
#lim = 10**(3-1)
L2=1
L1=1
F = L2+L1
i=3
while(F<lim):
  L2 = L1
  L1 = F
  F = L2+L1
  i+=1
  #print i,F
print i
