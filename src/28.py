#!/usr/bin/env python

import numpy as np
import util

max_side = 1001

# Strategy:
#   There are four corners for each expanding box, each at a fixed interval.
#   So just add the side length of each box four times to get the corners.
#   Then accumulate them.

n = 1
accum = n
for side in range(3,max_side+1,2):
  for corner in ['bottom_right','bottom_left','top_left','top_right']:
    n += side-1
    accum += n

print accum
