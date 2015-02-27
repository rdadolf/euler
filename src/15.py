#!/usr/bin/env python

import numpy as np
import util
import math

# The number of paths is equal to the sum of the paths which lead to a vertex.
v = 21 # 20x20-edge grid
#  1  1  1  1 ...
#  1  2  3  4 ...
#  1  3  6 10 ...
#  1  4 10 20 ...
#  .  .  .  . .  
#  .  .  .  .  . 
#  .  .  .  .   .

# These are even-powered binomials, and can be computed directly with the
# binomial theorem.
n = 2*(v-1)
k = v-1 

coef = math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
print coef
