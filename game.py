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


box = BoxShape.create(0.8, 0.8, 0.8)
box.setPosition(Vector3(0, 2, -3))

box2 = BoxShape.create(0.8, 0.8, 0.8)
box2.setPosition(Vector3(0, 2, -3))

# Apply an emissive textured effect (no lighting)
box.setEffect("textured -v emissive -d cyclops/test/omega-transparent.png")
box2.setEffect("textured -v emissive -d cyclops/test/omega-transparent.png")

getDefaultCamera().addChild(box2)

uim = UiModule.createAndInitialize()

hud = Container.create(ContainerLayout.LayoutVertical, uim.getUi())
hud.setStyle('fill: #00000080')
l1 = Label.create(hud)
l2 = Label.create(hud)
l3 = Label.create(hud)

l1.setFont('fonts/arial.ttf 20')
l1.setText("Heads up display test")

l2.setFont('fonts/arial.ttf 14')
l2.setText("Camera position:")

l3.setFont('fonts/arial.ttf 14')

# enable 3d mode for the hud container and attach it to the camera.
c3d = hud.get3dSettings()
c3d.enable3d = True
c3d.position = Vector3(0, 2.5, -2.5)
# Rotate the hud a little. Note that rotation needs to be specified
# as a vector.
c3d.normal = quaternionFromEulerDeg(0,-30,0) * Vector3(0,0,1)
# Scale is the conversion factor between pixels and meters
c3d.scale = 0.004
c3d.node = getDefaultCamera()

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
            #x = math.sqrt( math.pow(dist,2) - math.pow(z,2))
            #print 'Player:', player, ' Item:', item, ' X:', pos.x, ' Z:', pos.z, 'x:', x, ' z:', z
            #print x
            #print z
            objects[player][item].setPosition(x, 2, z)


    #getDefaultCamera().pitch(dt)
	#box.yaw(dt / 3)

setUpdateFunction(onUpdate)
