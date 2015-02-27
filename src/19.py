#!/usr/bin/env python

import numpy as np
import util
import datetime

# I am not really feeling like implementing my own calendar nonsense.
# So I'll just use what is already built.

start = datetime.datetime(1901,1,1)
timedelta = datetime.timedelta(1)
end = datetime.datetime(2000,12,31)

d = start
n = 0
while d<=end:
  if d.weekday()==6 and d.day==1:
    n+=1
  d += timedelta

print n
