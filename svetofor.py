# -*-coding:utf8;-*-
# qpy:console
# qpy:2

import time, math

class Svetofor():


    def __init__(self, red_interval=5.0, green_interval=10.0, red2green_fixed=time.time()):
        self.time_left = 0.0
        self.red2green_fixed = red2green_fixed if red2green_fixed else time.time()
        self.red_interval = red_interval
        self.green_interval = green_interval
        self.cycle = self.green_interval + self.red_interval

    def check(self):
        cycles = int(math.floor((time.time() - self.red2green_fixed) / (self.cycle)))
        since_last = time.time() - cycles * self.cycle - self.red2green_fixed
        self.status = (since_last) < self.green_interval
        self.time_left = self.status and self.green_interval - since_last or self.cycle - since_last
        return self.status

    def correct_rg(self):
        self.red2green_fixed = time.time()

    def correct_gr(self):
        self.red2green_fixed = time.time() - self.green_interval
    def export(self):
        return ';'.join(map(str,[self.red_interval,self.green_interval,self.red2green_fixed]))
