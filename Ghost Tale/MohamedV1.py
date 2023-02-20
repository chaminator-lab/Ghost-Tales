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
map = lines()[1].split()
MapXY.append(int(map[0]))
MapXY.append(int(map[1]))

# ICI LINA ET CHARLOTTE
#Take orders from player and stock them in alist
def getOrderslist():
    print("give orders YOU IDIOT")
    orders=input()
    orderslist = orders.split()
    return orderslist
print(getOrderslist())

def runActions(OrderList = getOrderslist()):
    ghost_first=True
    for order in OrderList:
        if order == "ghost" and ghost_first==True:
            Invokeghost()
        else:

#Fini LINA ET CHARLOTTE

#Initialise le dictionnaire et la liste des cases magique
def getMagicDict():
  #Initialise MagicDict
  MagicDict = {}
  #Set MagicDict
  for i in range(6 , len(lines())):
      splitLine = lines()[i].split()
      MagicDict[(int(splitLine[0]), int(splitLine[1]))]= int(splitLine[2])
  return MagicDict
def getMagicList():
 #Initialise Magiclist
    MagicList=[]
    for i in range(6 , len(lines())):
      splitLine = lines()[i].split()
      MagicList.append((int(splitLine[0]), int(splitLine[1])))
    return MagicList


#Initialise les premier phantomes de debut de partie et sauvegarde la ou les fantomes apparaissent
#Pour chaque joueur dans une clé "ghostPopLocation"
def setInitialGhostsAndPopSpot():
    """
    spawns the ghost of each player (free of charges :D) which has 100 health points (HP)
    
    returns:
        Players: each player has now one ghost to their name in their own dictionary
    """
  ghost1 = lines()[3].split()
  ghost2 = lines()[4].split()
  Players[1]["ghosts"][(int(ghost1[1]), (int(ghost1[2])))] =  100
  Players[1]["ghostPopLocation"]= (int(ghost1[1]),int(ghost1[2]))
  Players[1]["ghostsLocationList"].append((int(ghost1[1]),int(ghost1[2])))
  Players[2]["ghosts"][(int(ghost2[1]), (int(ghost2[2])))] =  100
  Players[2]["ghostPopLocation"]= (int(ghost2[1]),int(ghost2[2]))
  Players[2]["ghostsLocationList"].append((int(ghost2[1]),int(ghost2[2])))
  return Players

#create board list and print board with ressources bar
def InitialBoardDisplay(MAP = getMap()):
    """
    displays the board of the game
    
    returns:
        BOARD: board of the game
    """
    BOARD = [[X+1,Y+1]for X in range(MAP[0]) for Y in range(MAP[1])]
    for cell in BOARD :
        if (cell[1]+cell[0])%((2+getMap()[1]+getMap()[0])/2) == 0:
            print(u'🟦' ,end ='')
        x= random.randint(0,2)
        if x == 0:
            print(u'🟩' ,end ='')
        else:
            print(u'🟫' ,end ='')
        if cell [1] == getMap()[1] :
            print('')
    print(P2+'\'s Ghosts       ⚔        '+P1+'\'s Heroes')
    print (u'💀🧛',u'\💉 ',Players[1]["score"],u'\🩸 ',Players[1]["magic"],end='')
    print(' |',Players[2]["magic"],u'🔮/ ',Players[2]["score"],u'🩹/ ' '' u'🧙‍♂️🏰\n',end='')
    return BOARD
#1 -ADD Ghost to players dict  and reduce magic points
def Invokeghost (Players,PlayerID):
    """
    each player can choose whether or not they want to buy another ghost for 300 magic points
    
    parameters:
        PlayerID: ID of the player who wants to buy a ghost (int)
        
    return:
        Players: newly bought ghost(s) is added to the player's dictionary
    """
    if Players[PlayerID]["magic"] >= 300 and not[Players[PlayerID]["ghostPopLocation"] in Players[PlayerID]["ghostsLocationList"]]:
        Players[PlayerID]["magic"] -= 300
        Players[PlayerID]["ghosts"][(Players[PlayerID]["ghostPopLocation"][0],Players[PlayerID]["ghostPopLocation"][1])] = 100
    return Players

#2- HEAL ghost with chosen amount and reduce twice the amount from magic
def Healghost(Players,PlayerID,targetGhost,amount):
    if targetGhost in Players[PlayerID]["ghostsLocationList"] and Players[PlayerID]["magic"] >= (amount*2):
       Players[PlayerID]["ghosts"][targetGhost] += amount
       Players[PlayerID]["magic"] -= (amount*2)
    return Players

#3- Collect the magic if ghost on spot and delete the magic cell from
#Magic Dictionnary and Magic list
def collectMagic (PlayersID,targetGhost):
    """
    if the ghost of a player steps on a tile filled with magic, the magic is collected by the player which will therefore remove the magic from the tile
    
    parameters:
        PlayersID: ID of the player (int)
        targetGhost: ghost that stepped on the magic-filled tile (str)
        
    returns:
        Players: the collected magic will be added to the player's dictionary
    """
    if targetGhost in getMagicList() :
        Magicdict =  getMagicDict()
        Magiclist = getMagicList()
        Players[PlayersID]["magic"] += Magicdict[targetGhost]
        #is using pop OK ?
        Magicdict.pop(targetGhost)
        Magiclist.remove(targetGhost)
        return Players
#4- MAKE A MOVE YOU STUPID GHOST <3, changes PLAYERS dict
#Para: Takes in current and futur location
# Changes the dict and moves the emo boiz before they start crying
#requiers
def moveGhost(ghostLocation,futureGhostLocation,PlayerID,Players):
    """
    move the ghost of a player according to the chosen direction
    
    parameters:
        ghostLocation: location of the ghost (int)
        futureGhostLocation: future location of the ghost after it got moved by the player (int)
        PlayerID: ID of the player who wants to move its ghost (int)
    
    return:
        Players: the player's dictionary is updated with its ghost new location
    """
    curr = ghostLocation
    Players[PlayerID]["ghostsLocationList"]


#5- Regen magic points to the player at the end of the round
def regenPlayer(PlayerID,Players) :
    """
    automatically give 10HP to each player at the end of each turn, plus 1 additional HP per surviving ghosts
    
    parameters:
        PlayersID: ID of the player which will receive the HP (int)
    
    returns:
        Players: the player's dictionary is updated with the added HP
    """
    Players[PlayerID]["magic"] += 10 
    return Players[PlayerID]["magic"]

print(setInitialGhostsAndPopSpot())
print(InitialBoardDisplay(MAP = getMap()))
print(Invokeghost(Players,1))
print(Healghost(Players,2,(19,19),20))
print(collectMagic(2,(19,19)))
print(regenPlayer(1,Pla
yers))



ghost 10-10:x12-10 
ghostattack(attacker,attackinSpot)
ghostattack((10,10),(12,10))
