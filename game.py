# basic omegalib script: just display a textured spinning cube.
from omega import *
from cyclops import *

import random
import math

nmbItems = 10
nmbPlayers = 3
objSpeed = 0.5 # per second
objStartingRadius = 5

random.seed()

objects=[]
for player in xrange(nmbPlayers):
    objects.append([])
    for item in xrange(nmbItems):
        x = random.randint(0, objStartingRadius) * (random.randint(0, 1) * 2 - 1)
        z = math.sqrt(math.pow(objStartingRadius,2) - math.pow(x,2)) * (random.randint(0, 1) * 2 - 1)
        objects[player].append( BoxShape.create(0.5, 0.5, 0.5) )
        objects[player][item].setPosition(Vector3(x, 2, z))


# Spin the box!
def onUpdate(frame, t, dt):
    for player in xrange(nmbPlayers):
        for item in xrange(nmbItems):
            pos = objects[player][item].getPosition()
            dist = math.sqrt( math.pow(pos.x,2) + math.pow(pos.z,2) )
            angle = math.asin( pos.z / dist )
            dist -= objSpeed * dt
            z = math.sin(angle) * dist
            x = math.cos(angle) * dist
            objects[player][item].setPosition(x, 2, z)

setUpdateFunction(onUpdate)
