#!/usr/bin/env python

import numpy as np
import util

ones_w = ['','one','two','three','four','five','six','seven','eight','nine']
teens_w = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens_w = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundred_w = 'hundredand'
ones = map(len,ones_w)
teens = map(len,teens_w)
tens = map(len,tens_w)
hundred = len(hundred_w)

# two-digit numbers
s_2d = 0
# 1-9
s_2d += sum(ones)
# 10-19
s_2d += sum(teens)
# 20-99
s_2d += len(ones)*sum(tens) + len(tens)*sum(ones)
#   hundred's digit,"hundredand",for 100,200..., all 2-digit numbers
s = 100*sum(ones) + 900*hundred - 9*len('and') + 10*s_2d
s += len('onethousand')

print s
