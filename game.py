# basic omegalib script: just display a textured spinning cube.
from omega import *
from cyclops import *

from player import *
from common import *
from itemManager import *
import random
from scoreboard import *

global dirAmount
global scoreBoard
global bananas



dirAmount = 0.01
nmbPlayers = 3
objSpeed = 0.5 # per second
objStartingRadius = 10

nmbItems = 4
timestep = 2
totalItems = 36

objHeight = 1.0

#enable physics
getSceneManager().setGravity(Vector3(0, -0.8, 0))
getSceneManager().setPhysicsEnabled(True)
colorDict = {1:'red', 2:'blue', 11:'green'}

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

activeWandIds = [-1] * 3

playerList=[]

scoreBoard = None


def printActiveWands():
    for wandId in activeWandIds:
        print wandId

def syncRandom(mySeed):
  print "Seeding with %d" % (mySeed)
  random.seed(mySeed)

# Spin the box!
hasRun = False
itemManager = ItemManager()

def moveInDir(dirInt, item, dt):
    #for letfhalf, move left

    currPos = item.getPosition()

    if dirInt == 0:
        item.setPosition(currPos + Vector3(-dt, -dt * 1.5, dt))

    #for right half, move right
    else:
        item.setPosition(currPos + Vector3(dt, -dt * 1.5, dt))


def onUpdate(frame, t, dt):
  #global hasRun
  #global scoreBoard

  #if t > 2.0 and not hasRun:
  #  for player in players:
  #    playerList.append( Player(nmbItems, objHeight, objStartingRadius, totalItems, timestep, player, 0) )

  #  if players:

  #      scoreBoard = ScoreBoard(playerList)

  itemManager.update(frame, t, dt)
  #for item in gameItems:
  #  item.update(dt)

  #for player in playerList:
  #  player.update(t, dt)

def spawn():
  itemManager.spawn()

def onEvent():
    global scoreBoard
    global dirAmount

    e = getEvent()
    sourceID = e.getSourceId()

    '''
    if sourceID not in activeWandIds:
        activeWandIds.append(sourceID)
        #playerList[sourceID].setWandId(activeWandIds[sourceID])
    '''

    if(e.getServiceType() == ServiceType.Pointer or e.getServiceType() == ServiceType.Wand):
        #confirmButton = EventFlags.Left

        #if(e.getServiceType() == ServiceType.Wand):
            #confirmButton = EventFlags.Button3

        #if(e.isButtonDown(confirmButton)):
        r = getRayFromEvent(e)
        #print 'confirm button is pressed'

        for item in gameItems:
            halfCount = -1
            for half in item.halves:
                hitData = hitNode(half, r[1], r[2])

                if(hitData[0]):
                    print 'player ', sourceID, 'Hit ', half,'!'
                    print 'Intersection at ', hitData[1]
                    half.setEffect('colored -e %s'%colorDict[sourceID])

                    moveInDir(0, item.halves[0], dirAmount)
                    moveInDir(1, item.halves[1], dirAmount)

                    scoreBoard.updateScore(sourceID, 1)



setUpdateFunction(onUpdate)
setEventFunction(onEvent)
