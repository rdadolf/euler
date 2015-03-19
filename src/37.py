#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

# Strategy:
#   Building right-truncatable primes is easy: just add certain digits to the
#     right and check for primality. Left-truncatable primes are similar,
#     except that different digits can be added to the left.
#   Building fully-truncatable primes is done by building left- or right-
#     truncatable primes, then checking for the opposite truncatability.
#   To enumerate them all, we need to follow a one-sided-truncatable chain
#     until it ends, even if intermediates are not fully truncatable.
#     For instance, building 3797 requires either the left-chain
#     3,37,379,3797 (in which 379 is not fully truncatable) or the right-chain
#     7,97,797,3797 (in which 97 is not fully truncatable). 

S = util.Sieve(1000000)

# Originally, I thought I had to go both ways. I do not, because the set of
# fully-truncatable primes is a subset of both the right-truncatable and left-
# truncatable primes, so I can choose either.

right_addable = [1,3,7,9]
left_addable = [1,2,3,5,7,9]

def right_add(p,d):
  # pp_ -> ppd
  return 10*p+d
#def left_add(p,d):
#  # _pp -> dpp
#  return int(str(d)+str(p))

#def right_truncatable(sieve, k):
#  # 3797 << 379_ << 37__ << 3___
#  while k>0:
#    if not sieve.is_prime(k):
#      return False
#    k//=10
#  return True
def left_truncatable(sieve, k):
  # 3797 >> _797 >> __97 >> ___7
  mod = 10
  rem = k%mod
  while k!=rem:
    if not sieve.is_prime(rem):
      return False
    mod *= 10
    rem = k%mod
  return sieve.is_prime(k)

t_primes = set([])

#rightmost = [3,7] # only these numbers can end a fully-truncatable prime
leftmost = [2,3,5,7] # but any prime can start it

left_partials = leftmost
#right_partials = rightmost
# Start from one side, add to the other
#while len(right_partials)>0 and len(left_partials)>0 and len(t_primes)<11:
while len(left_partials)>0 and len(t_primes)<11:
  # Build right from left_partials (naturally right-truncatable)
  #print 'Old Left Parts',left_partials
  #print 'Left Candidates',list(itertools.chain(*[ [right_add(lpart,rdigit) for rdigit in right_addable] for lpart in left_partials]))
  left_partials = filter(S.is_prime, itertools.chain(*[ [right_add(lpart,rdigit) for rdigit in right_addable] for lpart in left_partials]))
  t_primes |= set(filter(lambda k:left_truncatable(S,k), left_partials))
  # Build left from right partials (naturally left-truncatable)
  #print 'Old Right Parts',right_partials
  #print 'Right Candidates',list(itertools.chain(*[ [left_add(rpart,ldigit) for ldigit in left_addable] for rpart in right_partials]))
  #right_partials = filter(S.is_prime, itertools.chain(*[ [left_add(rpart,ldigit) for ldigit in left_addable] for rpart in right_partials]))
  #t_primes |= set(filter(lambda k:right_truncatable(S,k), right_partials))

  #print 'PROGRESS(',len(t_primes),'):',t_primes

#print t_primes
print sum(t_primes)
