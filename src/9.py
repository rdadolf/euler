#!/usr/bin/env python

import numpy as np

# There are a maximum of ~1000000 pairs for a and b, loose upper bound
# Brute force all pairs (computing c to complete the pythagorean triple)

ones = np.zeros(999)+1
a=np.outer(ones,np.arange(1,1000))
b=np.outer(np.arange(1,1000),ones)
c=np.sqrt(a*a+b*b)
s=a+b+c
p=a*b*c
print int(p[np.where(s==1000)][0])

