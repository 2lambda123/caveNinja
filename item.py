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
    self.initialPosition = getRandomPosition(0, r)
    norm = copy.copy(self.initialPosition)
    norm.normalize()
    self.force.x = -1 * norm.x
    self.force.z = -1 * norm.z

    iIdx = randint(0, 1)
    pIdx = randint(0, 2)
    self.item = StaticObject.create( items[players[pIdx]][iIdx] )
    self.item.setPosition( self.initialPosition )
    self.item.setEffect("textured")
    self.item.getRigidBody().initialize(RigidBodyType.Box, 1)
    self.item.getRigidBody().applyImpulse(self.force, self.relativePosition)
    #item.getRigidBody().setUserControlled(True)
    self.item.getRigidBody().sync()

  def originCheck(self):
    pos = self.item.getPosition()
    if pos.x > -2 and pos.x < 2 and pos.z > -2 and pos.z < 2 :
      #resetPosition
      self.item.setPosition( getRandomPosition(self.height, self.radius) )
      #reset speed
      self.objSpeed = random.random() * 0.2 + 0.3

#  def update(self, dt):
    #self.originCheck()
    #pos = self.item.getPosition()
    #dist = sqrt( pow(pos.x,2) + pow(pos.z,2) )
    #angleZ = asin( pos.z / dist )
    #angleX = acos( pos.x / dist )
    #dist -= self.objSpeed * dt
    #z = math.sin(angleZ) * dist
    #x = math.cos(angleX) * dist
    #self.item.setPosition(x, self.height, z)
    #self.item.getRigidBody().sync()

