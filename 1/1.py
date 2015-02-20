#!/usr/bin/env python

# sum of multiples of 3 and 5 below 1000
# = (3+6+9+...) + (5+10+15+...) - (15+30+45+...)
# = 3*(1+2+3...) + 5*(1+2+3+...) - 15*(1+2+3+...)

upper = 1000

range3 = (upper-1)//3
range5 = (upper-1)//5
range15 = (upper-1)//15
#print (range3,range5,range15)

def sum_nats(n):
  return n*(n+1)/2

s = 3*sum_nats(range3) + 5*sum_nats(range5) - 15*sum_nats(range15)

print s
