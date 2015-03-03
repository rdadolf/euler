#!/usr/bin/env python

import numpy as np
import util

# This is a bit faster than the lambda/str version. I just don't like waiting.
def digit_sum(n):
  s = 0
  for d in xrange(0,6):
    s += (n%10)**5
    n //= 10
  return s

accum = 0
# 7*9^5 has only 6 digits, so no 7-digit number can be produced by fifth powers
max_n = 6*(9**5)

for n in xrange(10,max_n):
  #digit_sum = sum(map(lambda x: int(x)**5, str(n)))
  if digit_sum(n) == n:
    accum += n
print accum
