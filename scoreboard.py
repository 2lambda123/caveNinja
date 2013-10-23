'''
Created on Oct 23, 2013

@author: Galen
'''
from omega import *
from omegaToolkit import *

class ScoreBoard:
    
    def __init__(self, players):
        self.numPlayers = len(players)        
        
        self.names = []
        
        wandIds = []
        
        for player in players:
            self.names.append(player.name)
            wandIds.append(player.wandId)
            
        self.wandIds = wandIds
        
        self.generateScoreboard()
        
    #Master function
    def generateScoreboard(self):
        ui = UiModule.createAndInitialize()
        wf = ui.getWidgetFactory()
        uiroot = ui.getUi()
        
        entryHeight = 30
        entryWidth = 200
        
        colors = ['red', 'blue', 'green']
        
        self.scoreContainer = wf.createContainer('scorecontainer', uiroot, ContainerLayout.LayoutFree)
        self.scoreContainer.setPosition(Vector2(12000,0))
        
        self.labels = []
        self.scores = []
        
        for i in xrange(0, self.numPlayers):
            #player names
            self.labels.append(wf.createLabel('label%i'%i, self.scoreContainer, names[i]))
            self.labels[i].setPosition(Vector2(0 ,i * entryHeight))
            self.labels[i].setColor(Color(colors[i]))
            
            #Player scores
            self.scores.append(wf.createLabel('score%i'%i, self.scoreContainer, player))
            self.scores[i].setPosition(Vector2(entryWidth ,i * entryHeight))
            self.scores[i].setColor(Color(colors[i]))

    def updateScore(self, playerId, value):
        score = int(self.scores[playerId])
        score += value
        self.scores[playerId].setText(str(score))
        
        
        
        

        
    