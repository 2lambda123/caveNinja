from omega import *
from cyclops import *
from common import *
from math import *
from random import *

from item import *

class ItemManager:

  maxItems = 10
  liveItems = []
  respawnTime = 0
  minTime = 0.2
  maxTime = 2
  elapsedTime = 0

  def __init__(self):
    self.respawnTime = rangef(self.minTime, self.maxTime)

  def spawn(self):
    #do nothing
    item = Item()

  def update(self, frame, t, dt):
    if isMaster():
      if self.elapsedTime > self.respawnTime :
        broadcastCommand("spawn()")
        self.elapsedTime = 0
        self.respawnTime = rangef(self.minTime, self.maxTime)

      self.elapsedTime += dt
