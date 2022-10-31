from egg import Egg
from ring import Ring


class EggRing(object):

    def __init__(self, x, y, t, sp):
        self.ovoid = Egg(x, y, t, sp)
        self.circle = Ring()
        self.circle.start(x, y - sp / 2)

    def transmit(self):
        self.ovoid.wobble()
        self.ovoid.display()
        self.circle.grow()
        self.circle.display()
        if not self.circle.on:
            self.circle.on = True
