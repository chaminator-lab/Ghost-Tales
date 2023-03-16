import os
import random
#import blessed
term=blessed.Terminal()

def getLines():
  """Opens the file and returns each line in a list """
  fh = open("Map.txt", "r")
  lines = fh.readlines()
  return lines

def initialiseMapXY():
  """Initialse Maplist.
  Parameters
 -----------
  map: list of strings

  Return
  -----------
  MapXY: Empty dictionary 
  """
  MapXY=[]
  map =  getLines()[1].split()
  MapXY.append(int(map[0]))
  MapXY.append(int(map[1]))  
  return MapXY

def getMagicDict():
   """Initialise MagicDict
   Parameters
   ----------
   MagicDict: empty dictionary

   Return
   ------
   MagicDict
   """
   MagicDict = {}
   for i in range(6 , len(getLines())):
      splitLine =  getLines()[i].split()
      MagicDict[(int(splitLine[0]), int(splitLine[1]))]= int(splitLine[2])
   return MagicDict


def getMagicList():
  """Initialise MagicLict
  Parameters
  MagicLict: empty list

  Return
  -------
  MagicLict
  """
  MagicList=[]
  for i in range(6 , len(getLines())):
      splitLine =  getLines()[i].split()
      MagicList.append((int(splitLine[0]), int(splitLine[1])))
  return MagicList

def setInitialGhostsAndPopSpot(Players,lines=getLines()):
  """
  Initializes the first ghosts at the start of the game and saves where the ghosts appear
  For each player in a "ghostPopLocation" key
  Parametres
  ----------
  ghost1 and ghost2: list of strings, the list contains the splitted items from lines (line 3 and line 4)

  Return
  -------
  Players: dictionary 
  """
  ghost1 = lines[3].split()
  ghost2 = lines[4].split()
  Players[1]["ghosts"][(int(ghost1[1]), (int(ghost1[2])))] =  100
  Players[1]["ghostPopLocation"]= (int(ghost1[1]),int(ghost1[1]))
  Players[1]["ghostsLocationList"].append((int(ghost1[1]),int(ghost1[2])))
  Players[2]["ghosts"][(int(ghost2[1]), (int(ghost2[2])))] =  100
  Players[2]["ghostPopLocation"]= (int(ghost2[1]),int(ghost2[1]))
  Players[2]["ghostsLocationList"].append((int(ghost2[1]),int(ghost2[2])))
  return Players

def returnCorrectMagicEmoji(magicValue):
   """Returns correct emoji
   Paramaters
   ----------
   MagicValueDict: Dictionary with key the amoutn of points and value the corresponding emoji
   Return
   ---------
   magicvalue: the correct emoji"""
   magicValueDict = {10:'🥨',30:'🍟',50:'🍜',100:'🌯',500:'🍺'}
   return magicValueDict[magicValue]

#PRINTINITIALY 
def printBoards(MapXY,MagicList,MagicDict,Players):
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #PRINT THE NUMBERS ON THE EDGES
    for x in range(1,MapXY[0]+1):
        if x == 1:
          print(term.move_xy(27,0)+term.on_color_rgb(255,255,255)+term.black+term.underline+term.bold+str(x)+term.normal+term.move_xy(50,50),end=' ',flush=True)
        else:
           if (x%2) == 0 :
             print(term.move_xy(25+(x*2),0)+term.on_color_rgb(0,0,0)+term.white4+term.underline+term.bold+str(x)+term.normal+term.move_xy(50,50),end='',flush=True)
           else :
             print(term.move_xy(25+(x*2),0)+term.on_color_rgb(255,255,255)+term.black+term.underline+term.bold+str(x)+term.normal+term.move_xy(50,50),end='',flush=True)
    for y in range(1,MapXY[1]+1):
        if (y%2) == 0 :
            print(term.move_xy(25+0,y)+term.white+term.underline+term.bold+str(y)+term.normal+term.move_xy(50,50),end='',flush=True)
        else :
            print(term.move_xy(25+0,y)+term.on_color_rgb(255,255,255)+term.black+term.underline+term.bold+str(y)+term.normal+term.move_xy(50,50),end='',flush=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #PRINT THE PLAYING BOARD WITH THE MAGICAL SPOTS
    BOARD = [(X,Y)for X in range(1,MapXY[0]+1) for Y in range(1,MapXY[1]+1)]
    for case in BOARD: 
        if ((case[0]+case[1])%2) == 0:
          print(term.move_xy(25+case[0]*2,case[1])+term.on_black+'  '+term.normal+term.move_xy(50,50),end='',flush=True)
        else:
          print(term.move_xy(25+case[0]*2,case[1])+term.on_color_rgb(34,230,100)+'  '+term.normal+term.move_xy(50,50),end='',flush=True)
        if  case in MagicList :
          magicValue=MagicDict[case]
          if (case[0]+case[1])%2 == 0 :
            print(term.move_xy(25+case[0]*2,case[1])+term.black+returnCorrectMagicEmoji(magicValue)+term.normal+term.move_xy(50,50),end='',flush=True)
          else :
            print(term.move_xy(25+case[0]*2,case[1])+term.on_color_rgb(34,230,100)+returnCorrectMagicEmoji(magicValue)+term.normal+term.move_xy(50,50),end='',flush=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    #Print the first ghosts from the dictionnary    
    for player in [1,2]:
       if player == 1 :
         print(term.move_xy(25+Players[player]['ghostPopLocation'][0]*2,Players[player]['ghostPopLocation'][1])+term.on_gold+'👺'+term.normal+term.move_xy(50,50),end ='',flush=True)
       else :
          print(term.move_xy(25+Players[player]['ghostPopLocation'][0]*2,Players[player]['ghostPopLocation'][1])+term.on_red3+'🧝'+term.normal+term.move_xy(50,50),end ='',flush=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #print P1 table 
    P1Template=[(x,y)for x in range(25) for y in range(21)]
    for case in P1Template:
       print(term.move_xy(case[0],case[1])+term.on_color_rgb(0,0,0)+' '+term.normal+term.move_xy(45,45),end='',flush=True)
    #print P2 table
    P2Template=[(27+MapXY[0]*2+x,y)for x in range(25) for y in range(21)]
    for case in P2Template:
      print(term.move_xy(case[0],case[1])+term.on_color_rgb(0,0,0)+' '+term.normal+term.move_xy(45,45),end='',flush=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #print P1  Ressources
    print(term.move_xy(7,0)+term.on_color_rgb(0,0,0)+term.underline+term.white+'PLAYER ONE'+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(0,0)+term.on_color_rgb(0,0,0)+'🧛💀'+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(0,2)+term.on_color_rgb(0,0,0)+'💉  :      '+str(Players[1]['magic'])+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(0,4)+term.on_color_rgb(0,0,0)+'👻  :      '+str(len(Players[1]['ghostsLocationList']))+term.normal+term.move_xy(45,45),end='',flush=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #print  P2 Ressources
    print(term.move_xy(25+MapXY[0]*2+7,0)+term.on_color_rgb(0,0,0)+term.underline+term.white+'PLAYER TWO'+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(25+MapXY[0]*2+21,2)+term.on_color_rgb(0,0,0)+':  🔮'+term.move_xy(25+MapXY[0]*2+10,2)+str(Players[2]['magic'])+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(25+MapXY[0]*2+22,0)+term.on_color_rgb(0,0,0)+'🏰🧝'+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(25+MapXY[0]*2+21,4)+term.on_color_rgb(0,0,0)+':  😇'+term.move_xy(25+MapXY[0]*2+10,4)+str(len(Players[2]['ghostsLocationList']))+term.normal+term.move_xy(45,45),end='',flush=True)

#UpdateGhostsPannelforP1andP2
# to add :JUMP TO COLUMN B ONCE YOU HAVE NO LINES IN COLUMN A
def updateGhostsPannel(Players,MapXY):

  for player in [1,2]:
      if player == 1 :
        startprint = 0
      else:
        startprint = 27+MapXY[0]*2
      for ghost in range(len(Players[player]['ghostsLocationList'])):
        print(term.move_xy(startprint,ghost+7)+term.on_white3+term.white3+'•'+str(Players[player]['ghostsLocationList'][ghost][0])+'-'+str(Players[player]['ghostsLocationList'][ghost][1])+':'+str(Players[player]['ghosts'][Players[player]['ghostsLocationList'][ghost]])+'%'+term.normal+term.move_xy(190,190),end='',flush=True)

def getOrderslist(MapXY):
    """Takes orders from players and stock them in a list
    Parameters
    ----------
    orderslistP1P2: empty dictionary
    Returns
    -------
    orderslistP1P2: dictionary with a list of the orders from the players"""
    orderslistP1P2=[]
    for player in [1,2]:
      if player == 1 :
        print(term.normal+term.move_xy(0,MapXY[1]+5)+"Player " + str(player) + " Insert your orders : \n"+term.move_xy(0,MapXY[1]+6)+term.clear_eol+term.red3,end='',flush=True)
        orders=input()
      else:
        print(term.normal+term.move_xy(27+MapXY[1]*2,MapXY[1]+5)+"Player " + str(player) + " Insert your orders : \n"+term.normal+term.move_xy(27+MapXY[1]*2,MapXY[1]+6)+term.clear_eol+term.blue3,end='',flush=True)
        orders=input()
      print(term.normal)
      orderslistP1P2.append(orders.split()) 
      
    return orderslistP1P2

def Invokeghost (Players,PlayerID):
    """Invoke a new ghost
    Parameters
    ----------
    Players: a dictionary
    PlayersID: ID of the players in the dictionary"""
    if Players[PlayerID]["magic"] >= 300 and (not(Players[PlayerID]["ghostPopLocation"] in Players[PlayerID]["ghostsLocationList"])):
        Players[PlayerID]["magic"] -= 300
        Players[PlayerID]["ghostsLocationList"].append((Players[PlayerID]["ghostPopLocation"][0],Players[PlayerID]["ghostPopLocation"][1]))
        Players[PlayerID]["ghosts"][(Players[PlayerID]["ghostPopLocation"][0],Players[PlayerID]["ghostPopLocation"][1])] = 100
        if PlayerID == 1:
          print(term.move_xy(25+Players[PlayerID]['ghostPopLocation'][0]*2,Players[PlayerID]['ghostPopLocation'][1])+term.on_blue+'👺'+term.normal+term.move_xy(50,50),end ='',flush=True)
        else:
          print(term.move_xy(25+Players[PlayerID]['ghostPopLocation'][0]*2,Players[PlayerID]['ghostPopLocation'][1])+term.on_blue+'😇'+term.normal+term.move_xy(50,50),end ='',flush=True)
    return Players


def updateMagicDisplay(Players,MapXY):
   
   print(term.move_xy(25+MapXY[0]*2+10,2)+str(Players[1]['magic'])+term.move_xy(70,70),end='',flush=True)
   print(term.move_xy(11,2)+str(Players[2]['magic'])+term.move_xy(70,70),end='',flush=True)


def updateGhostsNumberDiplay(Players,MapXY):
   
   print(term.move_xy(11,4)+str(len(Players[1]['ghostsLocationList']))+term.normal+term.move_xy(70,70),end='',flush=True)
   print(term.move_xy(25+MapXY[0]*2+10,4)+str(len(Players[2]['ghostsLocationList']))+term.normal+term.move_xy(70,70),end='',flush=True)



   
def playgame():
  print(term.home+term.clear)
  game_over=False
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

#Initialise  Maplist
  MapXY=initialiseMapXY()  
#Initialise MagicDict and Magiclist
  MagicDict = getMagicDict()
  MagicList=getMagicList()
  setInitialGhostsAndPopSpot(Players,getLines())
  printBoards(MapXY,MagicList,MagicDict,Players)
  updateGhostsPannel(Players,MapXY)
  while game_over == False:
     orders = getOrderslist(MapXY)
     #GHOST BUYING PHASE
     for i in [0,1]:
       if 'ghost' in orders[i]:
         Invokeghost(Players,i+1)
         updateMagicDisplay(Players,MapXY)
         updateGhostsNumberDiplay(Players,MapXY)
         updateGhostsPannel(Players,MapXY)
     #GHOST HEALING PHASE



playgame()