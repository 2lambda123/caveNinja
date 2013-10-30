from omega import *
from cyclops import *
from common import *
from math import *
from random import *
import copy

class Item:

  force = Vector3(0, 1.9, 1)
  relativePosition = Vector3(0, 0, 0)
  initialPosition = Vector3(0, 0, -6)

  fMinY = 1.5
  fMaxY = 2.0

  rMin = -0.2
  rMax = 0.2

  iMinR = 5.0
  iMaxR = 6.0
  item = None

  def __init__(self):
    #Assign a model
    self.force.y = rangef(self.fMinY, self.fMaxY)
    self.relativePosition.x = rangef(self.rMin, self.rMax)
    self.relativePosition.y = rangef(self.rMin, self.rMax)
    self.relativePosition.z = rangef(self.rMin, self.rMax)



    r =  rangef(self.iMinR, self.iMaxR)
    iIdx = randint(0, 1)
    pIdx = randint(0, 2)
    #self.item = StaticObject.create( items[players[pIdx]][iIdx] )
    #self.item.setPosition( self.initialPosition )
    #self.item.setEffect("textured")
    #self.item.getRigidBody().initialize(RigidBodyType.Box, 1)
    #self.item.getRigidBody().applyImpulse(self.force, self.relativePosition)
    #item.getRigidBody().setUserControlled(True)
    #self.item.getRigidBody().sync()
    self.halves = createRandomItem(playerName, r, self.force, self.relativePosition)


    self.parentHalf = self.halves[0]

    self.parentHalf.addChild(self.halves[1])
    self.halves[1].setPosition(Vector3(0,0,0))

    #if 'banana' in self.halves[1].getName():
    self.halves[1].setScale(Vector3(1.2,1.2,1.2))


    #scene.addChild(self.item)
    #self.item.setSelectable(True)

  def originCheck(self):
    pos = self.parentHalf.getPosition()
    if pos.x > -2 and pos.x < 2 and pos.z > -2 and pos.z < 2 :
      #resetPosition
      self.parentHalf.setPosition( getRandomPosition(self.height, self.radius))
      self.parentHalf.setEffect('textured')
      #reset speed
      self.objSpeed = random.random() * 0.2 + 0.3

  def resetPosition(self):
    self.parentHalf.setPosition( getRandomPosition(self.height, self.radius))
    self.parentHalf.setEffect('textured')
    self.halves[1].setEffect('textured')
    #reset speed
    self.objSpeed = random.random() * 0.2 + 0.3