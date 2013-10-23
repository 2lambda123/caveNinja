# basic omegalib script: just display a textured spinning cube.
from omega import *
from cyclops import *

from player import *
from common import *

nmbPlayers = 3
objSpeed = 0.5 # per second
objStartingRadius = 10

nmbItems = 4
timestep = 2
totalItems = 36

objHeight = 1.0

#random.seed()
if isMaster():
  random.seed()
  mySeed = random.randint(0, 1000000)
  broadcastCommand("syncRandom(%d)" % (mySeed))

# create a light
light1 = Light.create()
light1.setColor(Color("#ffffff"))
light1.setAmbient(Color("#444444"))
light1.setEnabled(True)

#load all the models
loadModels()

playerList=[]
def syncRandom(mySeed):
  print "Seeding with %d" % (mySeed)
  random.seed(mySeed)

# Spin the box!
hasRun = False

def onUpdate(frame, t, dt):
  global hasRun
  if t > 2.0 and not hasRun:
    for player in players:
      playerList.append( Player(nmbItems, objHeight, objStartingRadius, totalItems, timestep, player) )
    hasRun = True

  for item in gameItems:
    item.update(dt)

  for player in playerList:
    player.update(t, dt)

setUpdateFunction(onUpdate)
