import random
import os
import string
choice = False
while choice == False:
    print("Player 1,Pick a name :")
    P1 = input()
    print("Player 2,Pick a name :")
    P2 = input()
    choice = True
#Initialise Players dictionary
Players = {
    1 : {
        "ghostPopLocation": () , 
        "ghosts": {},
        "ghostsLocationList": [],
        "magic": 500,
        "score" : 0,
        
    },
    2 : {
        "ghostPopLocation": () ,
        "ghosts": {},
        "ghostsLocationList": [],
        "magic": 500,
        "score" : 0
    }
  }
# Open file and store each line in lines
#    //FILE PATH TO CORRECT //
fh = open("Map.txt", "r")
lines = fh.readlines()

#Initialise  Maplist
MapXY=[]
map = lines[1].split()
MapXY.append(int(map[0]))
MapXY.append(int(map[1]))


#Take orders from player and stock them in alist
def getOrderslist():
    print("give orders YOU <3")
    orders=input()
    orderslist = orders.split()
    return orderslist
print(getOrderslist())

def runActions(PlayerID,OrderList = getOrderslist()):
    if OrderList[0] == "ghost":
        Invokeghost()
    else:
        for order in OrderList:
            splitted=order.split(':') [r1-c1,xr2-c2]
            if splitted[1][0] == "x":
                #call splitry function [long ass file name in folder]
                from_to=transformOrder(splitted)
                fromhere = from_to[0]
                tohere = from_to[1]
                AttackGhost(PlayerID,fromhere,tohere)
            elif splitted[1][0] == "@":
                from_to=transformOrder(splitted)
                fromhere = from_to[0]
                tohere = from_to[1]
                moveGhost(PlayerID,fromhere,tohere)
            elif splitted[1][0] == "+":
                from_to=transformOrder(splitted)
                thisghost = from_to[0]
                amount=from_to[1]
                Healghost(PlayerID,thisghost,amount) 
            elif splitted[1][0] == "$":
                from_to=transformOrder(splitted)
                fromhere = from_to[0]
                collectMagic(PlayerID,fromhere)



oken = ["21-1","x12-29"]
def transformOrder (splitted):

    firsthalflist=splitted[0].split("-")
    firstTuple=(int(firsthalflist[0]),int(firsthalflist[1]))
    lol = splitted[1][0+1:]
    secondHalfList=lol.split("-")
    secondTuple=(int(secondHalfList[0]),int(secondHalfList[1]))
    fulltuple= [firstTuple,secondTuple]
    return fulltuple     
print(transformOrder(oken))



#Initialise le dictionnaire et la+- liste des cases magique

  #Initialise MagicDict and Magiclist
MagicDict = {}
MagicList=[]
  #Set MagicDict
for i in range(6 , len(lines)):
      splitLine = lines[i].split()
      MagicDict[(int(splitLine[0]), int(splitLine[1]))]= int(splitLine[2])
      MagicList.append((int(splitLine[0]), int(splitLine[1])))


#Initialise les premier phantomes de debut de partie et sauvegarde la ou les fantomes apparaissent
#Pour chaque joueur dans une clé "ghostPopLocation"
def setInitialGhostsAndPopSpot():
  ghost1 = lines[3].split()
  ghost2 = lines[4].split()
  Players[1]["ghosts"][(int(ghost1[1]), (int(ghost1[2])))] =  100
  Players[1]["ghostPopLocation"]= (int(ghost1[1]),int(ghost1[2]))
  Players[1]["ghostsLocationList"].append((int(ghost1[1]),int(ghost1[2])))
  Players[2]["ghosts"][(int(ghost2[1]), (int(ghost2[2])))] =  100
  Players[2]["ghostPopLocation"]= (int(ghost2[1]),int(ghost2[2]))
  Players[2]["ghostsLocationList"].append((int(ghost2[1]),int(ghost2[2])))
  return Players
def AttackGhost():
    return None

#create board list and print board with ressources bar
def InitialBoardDisplay(MAP):
    BOARD = [(X+1,Y+1)for X in range(MAP[0]) for Y in range(MAP[1])]
    for cell in BOARD :
        if (cell[1]+cell[0])%((2+MAP[1]+MAP[0])/2) == 0:
            print(u'🟦' ,end ='')
        if cell [1] == MAP[1] :
            print('')
        elif cell in MagicList:
            if MagicDict[cell]==10:
                print(u'🦴',end='')
            elif MagicDict[cell]==30:
                print(u'🥨',end='')
            elif MagicDict[cell]==50:
                print(u'🌯',end='')
            elif MagicDict[cell]==100:
                print(u'🍜',end='')
            else :
                print(u'🍟',end='')

        else :
            x= random.randint(0,2)
            if x == 0:
             print(u'🟩' ,end ='')
            else:
             print(u'🟫' ,end ='')
        

    print(P2+'\'s Ghosts       ⚔        '+P1+'\'s Heroes')
    print (u'💀🧛',u'\💉 ',Players[1]["score"],u'\🩸 ',Players[1]["magic"],end='')
    print(' |',Players[2]["magic"],u'🔮/ ',Players[2]["score"],u'🩹/ ' '' u'🧙‍♂️🏰\n',end='')
    return BOARD
#1 -ADD Ghost to players dict  and reduce magic points
def Invokeghost (PlayerID):
    if Players[PlayerID]["magic"] >= 30 and not[Players[PlayerID]["ghostPopLocation"] in Players[PlayerID]["ghostsLocationList"]]:
        Players[PlayerID]["magic"] -= 30
        Players[PlayerID]["ghosts"][(Players[PlayerID]["ghostPopLocation"][0],Players[PlayerID]["ghostPopLocation"][1])] = 100
    return Players

#2- HEAL ghost with chosen amount and reduce twice the amount from magic
def Healghost(PlayerID,targetGhost,amount):
    if targetGhost in Players[PlayerID]["ghostsLocationList"] and Players[PlayerID]["magic"] >= (amount*2):
       Players[PlayerID]["ghosts"][targetGhost] += amount
       Players[PlayerID]["magic"] -= (amount*2)
    return Players

#3- Collecte the magic if ghost on spot and delete the magic cell from
#Magic Dictionnary and Magic list
def collectMagic (PlayersID,targetGhost):
    if targetGhost in MagicList :
        Magicdict =  MagicDict
        Magiclist = MagicList
        Players[PlayersID]["magic"] += Magicdict[targetGhost]
        #is using pop OK ?
        Magicdict.pop(targetGhost)
        Magiclist.remove(targetGhost)
        return Players
#4- MAKE A MOVE YOU STUPID GHOST <3, changes PLAYERS dict
#Para: Takes in current and futur location
# Changes the dict and moves the emo boiz
#requiers

def moveGhost(PlayerID,ghostLocation,futureGhostLocation,Players):
    curr = ghostLocation
    Players[PlayerID]["ghostsLocationList"]


#5- Regen magic points to the player at the end of the round
def regenPlayer(PlayerID,Players) :
    Players[PlayerID]["magic"] += 10 
    return Players[PlayerID]["magic"]

def displayWinner():
    return None





setInitialGhostsAndPopSpot()
InitialBoardDisplay(MapXY)
Invokeghost(Players,1)
Healghost(Players,2,(19,19),20)
collectMagic(2,(19,19))
regenPlayer(1,Players)


