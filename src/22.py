#!/usr/bin/env python

import numpy as np
import util

raw_names = open('22_names.txt').read()
names = sorted(map(lambda s:s.strip('"'), raw_names.split(',')))
cscores = dict([(c,i+1) for (i,c) in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')])

print sum( [sum(map(lambda c:cscores[c], name))*(rank+1) for (rank,name) in enumerate(names)] )
