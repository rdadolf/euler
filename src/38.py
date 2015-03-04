#!/usr/bin/env python

import numpy as np
import util
import itertools

# the answer must be >918273645 and <987654321
#   that means ~35900 orders to consider
# 9 is the only 1-digit starting sequences
# 91->98 are the only 2-digit starting sequences
#   these give the wrong number of digits (2+3+3=8 or 2+3+3+3=11)
# 918->987 are the only 3-digit starting sequences
#   these give the wrong number of digits (3+4=7 or 3+4+4=11)
# 9182->9876 are the only 4-digit starting sequences
#   these are possible (4+5=9)
# 5-digit starting sequences are not possible

# So we just need to check whether n[0:4]==2*n[4:]

for order in itertools.permutations(['9','8','7','6','5','4','3','2','1'],9):
  n = int(''.join(order))
  if n<918273645:
    break
  a = int(''.join(order[0:4]))
  b = int(''.join(order[4:]))
  if 2*a==b:
    print n
    break
