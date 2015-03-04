#!/usr/bin/env python

import numpy as np
import util
import itertools
import sys

numbers = ['1','2','3','4','5','6','7','8','9']
s = 0
prods = set([])
for order in itertools.permutations(numbers,9):
  # if a x b = c
  # constraints: (Lx = len(str(x)))
  #   La < Lb
  #   La+Lb-1 <= Lc <= La+Lb
  #   La+Lb+Lc = 9
  # So the only possibilities are:
  #   La  Lb  Lc
  #   1   4   4
  #   2   3   4
  for (La,Lb,Lc) in [(1,4,4),(2,3,4)]:
    a = int(''.join(order[0:La]))
    b = int(''.join(order[La:La+Lb]))
    c = int(''.join(order[La+Lb:]))
    #print '%d x %d = %d'%(a,b,c)
    if a*b==c:
      #print '%d x %d = %d'%(a,b,c)
      prods.add(c)
print sum(prods)
