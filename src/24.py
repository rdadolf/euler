#!/usr/bin/env python

import numpy as np
import util
import math

# Choices for a k-digit number, k!
# We want the millionth number 10-digit number.
# Sanity check: 10! == 3628800 > 1000000
# Basic idea:
#   count how many choices there are for a k-1 digit number.
#   that is index of the digit from the list of available numbers
#   

n = 999999 # 0-indexed (i.e.- if n is 0, we get 0123456789, which is the "1st")
choices = np.zeros(10,dtype='i64')
for (i,digits) in enumerate(range(9,-1,-1)):
  f = math.factorial(digits)
  #print i, n, f, n//f, f*(n//f)
  choices[i] = n//f
  n -= f*(n//f)
#print choices

# now choose those digits (without replacement) from the list
digits = [0,1,2,3,4,5,6,7,8,9]
num = []
for c in choices:
  num.append(digits[c])
  #print digits[c]
  digits = digits[0:c]+digits[c+1:]
  #print digits
print ''.join(map(str,num))
