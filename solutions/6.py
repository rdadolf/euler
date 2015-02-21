#!/usr/bin/env python

import numpy as np

high=100
nums = np.arange(1,high+1)
sum_of_sq = np.sum(nums*nums)
sq_of_sum = np.sum(nums)**2

print sq_of_sum-sum_of_sq
