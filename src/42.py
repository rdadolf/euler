#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

values = {a:v+1 for (v,a) in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
def word_value(w):
  return sum([values[a] for a in w])
assert word_value('SKY')==55

words = map(lambda s:s.strip('"'),open('42_words.txt').read().split(','))
all_wvs = np.array(map(word_value,words),dtype='int64')

# Way 1: Brute force
# Just compute enough triangular numbers and check for inclusion
def w1():
  n = np.arange(1,np.max(all_wvs)+1)
  trinums = set(n*(n+1)/2)
  #assert 55 in trinums
  return sum([wv in trinums for wv in all_wvs])

# Way 2: Backcompute
# Check whether the word value is an integral triangular number
# (i.e.- t_10, not t_10.257)

# v = n(n+1)/2
# 0 = n^2 + n - 2v
# quadratic formula
# n = (-1 +- sqrt(1 - 4(-2v)))/2
# n = (sqrt(1+8v)-1)/2
def w2():
  roots = (np.sqrt(1+8*all_wvs)-1)/2
# int(n)=?n
  return np.count_nonzero(roots == np.array(roots,dtype='int64'))

#import timeit
#print 'Way 1',timeit.timeit(w1,number=10000)
#print 'Way 2',timeit.timeit(w2,number=10000)
# Turns out w2 is 10x faster! Nifty.
print w2()
