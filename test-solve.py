#!/usr/bin/env python

import subprocess as sub
import threading
import os.path
import json

import subprocess, threading

# Credit goes to "jcollado" at:
# http://stackoverflow.com/questions/1191374/subprocess-with-timeout
class Command(object):
  def __init__(self, cmd):
    self.cmd = cmd
    self.process = None
    self.out = ''
    self.err = ''

  def run(self, timeout):
    def target():
      self.process = sub.Popen(self.cmd, shell=True, stdout=sub.PIPE, stderr=sub.PIPE, cwd='src')
      (out, err) = self.process.communicate()
      self.out = out.strip()
      self.err = err.strip()
    thread = threading.Thread(target=target)
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
      self.process.terminate()
      thread.join()
    return (self.out,self.err)

def check_solution(k,v):
  (guess,err) = Command(k+'.py').run(timeout=60)
  #(guess,err) = Command(os.path.join('src',k)+'.py').run(timeout=60)
  if err!='':
    print 'Error:',err
  assert guess==v, 'Answer mismatch:\n\tguess:"%s"\n\tactual:"%s"'%(guess,v)

def test_solutions():
  d=json.load(open('solutions.json'))
  for (k,v) in json.load(open('solutions.json')).items():
    yield check_solution, k, v
