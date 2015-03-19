#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

# There are 10^6-10^5 6-digit numbers. We only need 10^6 digits. This is plenty.
max_i = 10**6//6 + 10**5

d='.'+''.join(map(str,xrange(1,max_i)))
assert d[12]=='1'
print np.prod(map(lambda n:int(d[n]), [1,10,100,1000,10000,100000,1000000]))
