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
  maxTime = 1
  elapsedTime = 0

  def __init__(self):
    self.respawnTime = rangef(self.minTime, self.maxTime)

  def spawn(self):
    #do nothing
    item = Item()
    gameItems.append(item)

  def update(self, frame, t, dt):
	if isMaster():
	  if self.elapsedTime > self.respawnTime :
		broadcastCommand("spawn()")
		self.elapsedTime = 0
		self.respawnTime = rangef(self.minTime, self.maxTime)

	self.elapsedTime += dt
	todel = []

	for item in gameItems:
	  if item.halves[0].getPosition().y < -2:
		todel.append(item)
		if(item.halves[0].getParent() != None):
			item.halves[0].getParent().removeChildByRef(item.halves[0])
		
	for item in todel:
		gameItems.remove(item)
