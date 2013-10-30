from omega import *
from cyclops import *
from omegaToolkit import *
from euclid import *
from math import *
import random

itemModel = {}
players = ['Andrew', 'Joshua', 'Antwan']
#players = ['Andrew']
items = {}
gameItems = []

items['Andrew'] = ['Chair', 'Table']
items['Joshua'] = ['banana', 'Table']
items['Antwan'] = ['SpaceShip', 'Table']

def getRandomPosition(y, radius):
  x = rangef(0, radius) * (random.randint(0, 1) * 2 -  1)
  z = sqrt(pow(radius,2) - pow(x,2)) * (random.randint(0, 1) * 2 - 1)
  return Vector3(x, y, z)

def loadModel(player, name):
  key = (player, name)
  itemModel[key] = ModelInfo()
  itemModel[key].name = name
  itemModel[key].path = "models/" + player + "/" + name + ".fbx"
  itemModel[key].size = 1.0
  getSceneManager().loadModel(itemModel[key])

def loadModels():
  for player in players:
    for item in items[player]:
      loadModel(player, item)

def createRandomItem(playerName, height, radius):
  index = random.randint(0, len(items[playerName]) - 1)

  item = StaticObject.create( items[playerName][index])
  #item = BoxShape.create(0.1, 0.1, 0.1)
  item.setPosition( getRandomPosition( height, radius ) )
  item.setEffect("textured")
  item.getRigidBody().initialize(RigidBodyType.Box, 1)
  force = Vector3(0, 3, -1)
  relativePosition = Vector3(0, 100, 0)
  item.getRigidBody().applyCentralImpulse(force)
  #item.getRigidBody().setUserControlled(True)
  item.getRigidBody().sync()



  #print item.getPosition()

  return item

def rangef(minf, maxf):
  return random.random() * maxf + minf



