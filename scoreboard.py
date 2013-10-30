'''
Created on Oct 23, 2013

@author: Galen
'''
from omega import *
from omegaToolkit import *
from euclid import *

class ScoreBoard:

    def __init__(self, players):
        self.numPlayers = len(players)

        self.names = []
        self.scores = {}

        wandIds = []

        for player in players:
            self.names.append(player.name)

        #head 0
        #batmna 1
        #robin 2
        #xbox 3
        #joker 11

        self.generateScoreboard()

    #Master function
    def generateScoreboard(self):
        ui = UiModule.createAndInitialize()
        wf = ui.getWidgetFactory()
        uiroot = ui.getUi()

        entryHeight = 60
        entryWidth = 200

        colors = ['red', 'blue', 'green']

        self.scoreContainer = wf.createContainer('scorecontainer', uiroot, ContainerLayout.LayoutFree)
        self.scoreContainer.setPosition(Vector2(13000,0))
        #self.scoreContainer.setPosition(Vector2(0,0))

        self.scoreContainer.setSize(Vector2(entryWidth * 2, entryHeight * len(self.names)))
        self.scoreContainer.setVisible(True)

        self.labels = []

        #for use with wand:
        wandIds = [1,2,11]

        #for use with mouse:
        #wandIds = [0,2,11]

        for i in xrange(0, self.numPlayers):
            #player names
            self.labels.append(wf.createLabel('label%i'%i, self.scoreContainer, self.names[i]))
            self.labels[i].setPosition(Vector2(0 ,i * entryHeight))
            self.labels[i].setColor(Color(colors[i]))
            self.labels[i].setVisible(True)
            self.labels[i].setFont('fonts/FuturaLT-Light.ttf %i'%entryHeight)


            #Player scores
            self.scores[wandIds[i]] = wf.createLabel('score%i'%i, self.scoreContainer, str(0))
            self.scores[wandIds[i]].setPosition(Vector2(entryWidth ,i * entryHeight))
            self.scores[wandIds[i]].setColor(Color(colors[i]))
            self.scores[wandIds[i]].setVisible(True)
            self.scores[wandIds[i]].setFont('fonts/FuturaLT-Light.ttf %i'%entryHeight)

    def updateScore(self, wandId, value):
        score = int(self.scores[wandId].getText())
        score += value
        self.scores[wandId].setText(str(score))







