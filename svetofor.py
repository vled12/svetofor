#-*-coding:utf8;-*-
#qpy:console
#qpy:2

import time, math

print time.time()

class Svetofor():
  time_left=0.0
  def __init__(self):
    self.status=True
    self.red2green_fixed=time.time()
    self.red_interval=5.0
    self.green_interval=10.0
    self.cycle= self.green_interval+self.red_interval
    
  def check(self):
    cycles=int(math.floor((time.time()-self.red2green_fixed)/(self.cycle)))
    since_last= time.time()-cycles*self.cycle-self.red2green_fixed
    self.status= (since_last)<self.green_interval
    self.time_left=self.status and self.green_interval-since_last or self.cycle-since_last
    return self.status
