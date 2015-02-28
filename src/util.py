import numpy as np

class Sieve():
  def __init__(self,upto=2):
    self._size = 3
    self._memo = np.zeros(self._size,dtype='int64')+1
    self._memo[0] = 0
    self._memo[1] = 0
    self._memo[2] = 1
    self._last_factor = 2
    self.gen(upto)

  def _alloc(self,upto):
    if upto>self._size:
      diff = upto-self._size
      self._memo = np.concatenate((self._memo, np.zeros(diff,dtype='int64')+1))
      self._size = upto

  def gen(self,upto):
    if(upto<=self._size):
      return
    self._alloc(upto)
    #print 'Sieving factors from %d to %d'%(self._last_factor,upto//2)
    for f in range(2, upto//2):
      # find next prime
      if self._memo[f]:
        #print 'Elimintating %d to %d by %d'%(f*2,self._size,f)
        self._memo[np.arange(f*2,self._size,f)] = 0
        self._last_factor = f

  def primes(self):
    return np.nonzero(self._memo)[0]

  def is_prime(self,n):
    if n>self._size:
      self.gen(n+1)
    return self._memo[n]

  def prime_factorization(self,n):
    self.gen(n) # get *at least* n
    fs = []
    ps = self.primes()
    for p in ps[ps<=n]:
      while n%p==0:
        fs.append(p)
        n = n/p
        if n==1:
          return fs
    assert False, 'Ran out of primes to test'

################################################################################

def factors(n):
  if(n<2):
    return [1]
  fs=[1,n]
  root_n=int(np.ceil(np.sqrt(n)))
  for i in xrange(2,root_n):
    if n%i==0:
      fs.append(i)
      if i!=n/i:
        fs.append(n/i)
  if root_n*root_n==n:
    fs.append(root_n)
  return fs


