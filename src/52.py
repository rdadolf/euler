#!/usr/bin/env python

import math
import itertools
import numpy as np
import util
import sys

def digits_of(n):
  return tuple(sorted(map(int,str(n))))

n=123456
while True:
  if len(set(map(digits_of, [n*s for s in [1,2,3,4,5,6]])))==1:
    print n
    sys.exit(0)
  n+=1
