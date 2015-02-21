#!/usr/bin/env python

import numpy as np

# Brute force all 3-digit products (about 1M numbers, easy).
# Sort them by size.
# Find the first palindromic number.

def is_palindromic(n): # only needs to handle 6-digit numbers
  return ( (n/100000%10)==(n/1%10) \
     and   (n/10000%10)==(n/10%10) \
     and   (n/1000%10)==(n/100%10) )

products = np.zeros((900,900))
inputs = np.arange(999,99,-1)
products = np.sort(np.outer(inputs,inputs).ravel())

i=0
while(not is_palindromic(products[-i])):
  i+=1

print products[-i]
