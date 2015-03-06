#!/usr/bin/env python

import math
import itertools
import numpy as np
import util

def is_palindromic_string(s):
  L = len(s)
  #print 'FWD',s[0:L/2]
  #print 'REV',s[-1:-(L/2)-1:-1]
  return s[0:L/2]==s[-1:-(L/2)-1:-1]
#for s in ['abcde','abcdef','abccba','abcdcba','a','']:
#  print s,is_palindromic_string(s)

def to_dec_str(n):
  return str(n)
def to_bin_str(n):
  return '{:b}'.format(n)

#print to_bin_str(585)

s=0
for n in xrange(1,1000000,2): # can't be even, since no leading zeros
  if is_palindromic_string(to_dec_str(n)) and \
     is_palindromic_string(to_bin_str(n)):
    #print n,to_bin_str(n)
    s+=n
print s
