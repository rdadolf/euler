#!/usr/bin/env python

import numpy as np
import util
import itertools
import sys

# sum(1->9)=45, which is divisible by 3, so no 9-digit pandigital number is prime
# sum(1->8)=36, which is divisible by 3, so no 8-digit pandigital number is prime

def number_from_digits(digits):
  p=len(digits)
  return sum([10**p * d for (p,d) in enumerate(reversed(digits))])

S=util.Sieve(7654322)
for d in range(7,3,-1):
  for order in itertools.permutations(range(d,0,-1),d):
    n = number_from_digits(order)
    if S.is_prime(n):
      print n
      sys.exit(0)
