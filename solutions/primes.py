import numpy as np

class Sieve():
  def __init__(self,upto=10):
    self._upto = max(upto+1,10)
    self._size = 3
    self._memo = np.zeros(self._size,dtype='int64')+1
    self._memo[0] = 0
    self._memo[1] = 0
    self._memo[2] = 1
    self._last_factor = 2
    self.gen(self._upto)

  def _alloc(self,upto):
    diff = upto-self._size
    self._memo = np.concatenate((self._memo, np.zeros(diff,dtype='int64')+1))
    self._size = upto

  def gen(self,upto):
    self._alloc(upto)
    #print 'Sieving factors from %d to %d'%(self._last_factor,upto//2)
    for f in range(2, upto//2):
      # find next prime
      if self._memo[f]:
        #print 'Elimintating %d to %d by %d'%(f*2,self._size,f)
        self._memo[np.arange(f*2,self._size,f)] = 0
        self._last_factor = f
    return self._last_factor

  def primes(self):
    return np.nonzero(self._memo)[0]

  def is_prime(self,n):
    if n<self._size:
      self.gen(n+1)
    return self._memo[n]

def prime_factorization(n):
  s=Sieve(n)
  fs = []
  for p in s.primes():
    #print p,n,n%p
    while n%p==0:
      fs.append(p)
      n = n/p
      if n==1:
        return fs
  assert False, 'Ran out of primes?'
