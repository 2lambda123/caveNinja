from omega import *
from cyclops import *
from common import *
from math import *

class Item:

  def __init__(self, scene, directory, scale, height, startingRadius, playerName):
    self.directory = directory
    self.height = height
    self.scale = scale
    self.radius = startingRadius
    # speed between 0.3 and 0.5
    self.objSpeed = random.random() * 0.2 + 0.3

    #Assign a model
    self.item = createRandomItem(playerName, height, startingRadius)
    
    #
    #scene.addChild(self.item)
    #self.item.setSelectable(True)

  def originCheck(self):
    pos = self.item.getPosition()
    if pos.x > -2 and pos.x < 2 and pos.z > -2 and pos.z < 2 :
      #resetPosition
      self.item.setPosition( getRandomPosition(self.height, self.radius) )
      #reset speed
      self.objSpeed = random.random() * 0.2 + 0.3

  def update(self, dt):
    self.originCheck()
    pos = self.item.getPosition()
    dist = sqrt( pow(pos.x,2) + pow(pos.z,2) )
    angleZ = asin( pos.z / dist )
    angleX = acos( pos.x / dist )
    dist -= self.objSpeed * dt
    z = math.sin(angleZ) * dist
    x = math.cos(angleX) * dist
    self.item.setPosition(x, self.height, z)

  def queryCallback(node, distance):
        print("Node " + node.getName() + " hit at " + distance)


'''
node = SceneNode.create('node')
getScene().addChild(node)
node.setSelectable(true)

# attach some stuff to the node...
# [ ... ]

def queryCallback(node distance):
    print("Node " + node.getName() + " hit at " + distance)

querySceneRay(Vector3f(0, 0, 0), Vector3f(0, 0, -1), queryCallback)
'''