# basic omegalib script: just display a textured spinning cube.
from omega import *
from cyclops import *

from player import *
from common import *
from scoreboard import *

nmbPlayers = 3
objSpeed = 0.5 # per second
objStartingRadius = 10

nmbItems = 4
timestep = 2
totalItems = 36

objHeight = 1.0

random.seed()

# create a light
light1 = Light.create()
light1.setColor(Color("#ffffff"))
light1.setAmbient(Color("#444444"))
light1.setEnabled(True)

#load all the models
loadModels()

activeWandIds = [-1] * 3

playerList=[]

count = 0
for player in players:
    playerList.append( Player(nmbItems, objHeight, objStartingRadius, totalItems, timestep, player, 0) )
    count += 1
    
#scoreBoard = ScoreBoard(playerList) 

def printActiveWands():
    
    for wandId in activeWandIds:
        print wandId

# Spin the box!
def onUpdate(frame, t, dt):
  for item in gameItems:
    item.update(dt)

  for player in playerList:
    player.update(t, dt)

def onEvent():
    e = getEvent()
    sourceID = e.getSourceId()
    
    if sourceID not in activeWandIds:
        activeWandIds.append(sourceID)
        #playerList[sourceID].setWandId(activeWandIds[sourceID])
        
    
    if(e.getServiceType() == ServiceType.Wand):
        confirmButton = EventFlags.Button3
        
        if(e.isButtonDown(confirmButton)):
            r = getRayFromEvent(e)
            print 'confirm button is pressed'
            
            for item in gameItems:
                hitData = hitNode(item.item, r[1], r[2])
                
                if(hitData[0]):
                    print 'player ', sourceID, 'Hit ', item.item,'!'
                    item.item.setEffect('colored -e red')
                    #scoreBoard.updateScore(sourceID, value)
                    
setUpdateFunction(onUpdate)
setEventFunction(onEvent)
