import os
import time
import random
import blessed
term=blessed.Terminal()
def getLines(map_path):#NATAN
  """Opens the file and returns each line in a list """
#    //FILE PATH TO CORRECT //

  fh = open(str(map_path), "r")
  lines = fh.readlines()
  return lines
#Initialise  Maplist
def initialiseMapXY(map_path):#NATAN
  """Initialse Maplist.
  Parameters
 -----------
  map: list of strings

  Return
  -----------
  MapXY: Empty dictionary 
  """
  MapXY=[]
  map =  getLines(map_path)[1].split()
  MapXY.append(int(map[0]))
  MapXY.append(int(map[1]))  
  return MapXY
#Initialise MagicDict
def getMagicDict(map_path):#NATAN
   """Initialise MagicDict
   Parameters
   ----------
   MagicDict: empty dictionary

   Return
   ------
   MagicDict
   """
   MagicDict = {}
   #Set MagicDict
   for i in range(6 , len(getLines(map_path))):
      splitLine =  getLines(map_path)[i].split()
      MagicDict[(int(splitLine[0]), int(splitLine[1]))]= int(splitLine[2])
   return MagicDict

def getMagicList(map_path):#NATAN
  """Initialise MagicLict
  Parameters
  MagicLict: empty list

  Return
  -------
  MagicLict
  """
  MagicList=[]
  for i in range(6 , len(getLines(map_path))):
      splitLine =  getLines(map_path)[i].split()
      MagicList.append((int(splitLine[0]), int(splitLine[1])))
  return MagicList

def setInitialGhostsAndPopSpot(Players,lines):#HABIB
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
  Players[1]["ghosts"][(int(ghost1[1]), (int(ghost1[2])))] =  10
  
  Players[1]["ghostPopLocation"]= (int(ghost1[1]),int(ghost1[2])
                                   )
  Players[1]["ghostsLocationList"].append((int(ghost1[1]),int(ghost1[2])))
  Players[2]["ghosts"][(int(ghost2[1]), (int(ghost2[2])))] =  10


  Players[2]["ghostPopLocation"]= (int(ghost2[1]),int(ghost2[2]))
  Players[2]["ghostsLocationList"].append((int(ghost2[1]),int(ghost2[2])))
  return Players

def returnCorrectMagicEmoji(magicValue):#LINA
   """Returns correct emoji
   Paramaters
   ----------
   MagicValueDict: Dictionary with key the amount of points and value the corresponding emoji
   Return
   ---------
   magicvalue: the correct emoji"""
   magicValueDict = {10:'🥨',30:'🍟',50:'🍜',100:'🌯',500:'🍺'}
   return magicValueDict[magicValue]

def returnCorrectGhostEmoji(PlayerID,case,health):#LINA
   """Returns correct emoji of the ghost according to the health of the ghost
   Parameters
   ----------
   case: coordinates of the location of the ghost
   Health: health of the ghost
   return
   -----
   emo: correct emoji"""
   healthValueDict = {1:("😇","👺"),2:("🧐","👹"),3:("😎","😈"),4:("😞","👿"),5:("😖","😡"),6:("💩","🤬")}
   if health == 100 :
      emo = healthValueDict[1][PlayerID]
   elif 100 > health and health > 75 :
      emo = healthValueDict[2][PlayerID]
   elif 75 >= health and health > 50 :
      emo = healthValueDict[3][PlayerID]
   elif 50 >= health and health > 35 :
      emo = healthValueDict[4][PlayerID]
   elif 35 >= health and health > 15 :
      emo = healthValueDict[5][PlayerID]
   elif 15 >= health and health > 0 :
      emo = healthValueDict[6][PlayerID]
   return emo

def printBoards(MapXY,MagicList,MagicDict,Players):#HABIB
    """print the board with all the atributes on it
    Parameters
    ----------
    MapXY:list with the coordinates of the board
    MagicList: List with the coordinates of the magic 
    """
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
          print(term.move_xy(25+case[0]*2,case[1])+term.on_color_rgb(44,95,45)+'  '+term.normal+term.move_xy(50,50),end='',flush=True)
        else:
          print(term.move_xy(25+case[0]*2,case[1])+term.on_color_rgb(173,223,173)+'  '+term.normal+term.move_xy(50,50),end='',flush=True)
        if  case in MagicList :
          magicValue=MagicDict[case]
          if (case[0]+case[1])%2 == 0 :
            print(term.move_xy(25+case[0]*2,case[1])+term.on_color_rgb(44,95,45)+returnCorrectMagicEmoji(magicValue)+term.normal+term.move_xy(50,50),end='',flush=True)
          else :
            print(term.move_xy(25+case[0]*2,case[1])+term.on_color_rgb(173,223,173)+returnCorrectMagicEmoji(magicValue)+term.normal+term.move_xy(50,50),end='',flush=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    #Print the first ghosts from the dictionnary    
    for player in [1,2]:
       if player == 1 :
         print(term.move_xy(25+Players[player]['ghostPopLocation'][0]*2,Players[player]['ghostPopLocation'][1])+returnCorrectGhostEmoji(player-1,Players[player]['ghostPopLocation'],Players[player]['ghosts'][Players[player]['ghostPopLocation']])+term.normal+term.move_xy(50,50),end ='',flush=True)
       else :
         print(term.move_xy(25+Players[player]['ghostPopLocation'][0]*2,Players[player]['ghostPopLocation'][1])+returnCorrectGhostEmoji(player-1,Players[player]['ghostPopLocation'],Players[player]['ghosts'][Players[player]['ghostPopLocation']])+term.normal+term.move_xy(50,50),end ='',flush=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #print P1 table 
    P1Template=[(x,y)for x in range(25) for y in range(21)]
    for case in P1Template:
       print(term.move_xy(case[0],case[1])+term.on_color_rgb(173,173,223)+' '+term.normal+term.move_xy(45,45),end='',flush=True)
    #print P2 table
    P2Template=[(27+MapXY[0]*2+x,y)for x in range(25) for y in range(21)]
    for case in P2Template:
      print(term.move_xy(case[0],case[1])+term.on_color_rgb(223,173,223)+' '+term.normal+term.move_xy(45,45),end='',flush=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #print P1  Ressources
    print(term.move_xy(7,0)+term.on_color_rgb(173,173,223)+term.underline+term.white+'PLAYER ONE'+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(0,0)+term.on_color_rgb(173,173,223)+'🏰🧝'+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(0,2)+term.on_color_rgb(173,173,223)+'🔮  :      '+str(Players[1]['magic'])+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(0,4)+term.on_color_rgb(173,173,223)+'😇  :      '+str(len(Players[1]['ghostsLocationList']))+term.normal+term.move_xy(45,45),end='',flush=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #print  P2 Ressources
    print(term.move_xy(25+MapXY[0]*2+7,0)+term.on_color_rgb(223,173,223)+term.underline+term.white+'PLAYER TWO'+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(25+MapXY[0]*2+21,2)+term.on_color_rgb(223,173,223)+':  💉'+term.move_xy(25+MapXY[0]*2+10,2)+str(Players[2]['magic'])+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(25+MapXY[0]*2+23,0)+term.on_color_rgb(223,173,223)+'🧛💀'+term.normal+term.move_xy(45,45),end='',flush=True)
    print(term.move_xy(25+MapXY[0]*2+21,4)+term.on_color_rgb(223,173,223)+':  👻'+term.move_xy(25+MapXY[0]*2+10,4)+str(len(Players[2]['ghostsLocationList']))+term.normal+term.move_xy(45,45),end='',flush=True)

def updateGhostsPannel(Players,MapXY):#HABIB
  """Updates the state of the board"""
  for player in [1,2]:
      if player == 1 :
        startprint = 0
        r=173
        g=173
        b=223
      else:
        startprint = 27+MapXY[0]*2
        r=223
        g=173
        b=223
      for ghost in range(len(Players[player]['ghostsLocationList'])):
        print(term.move_xy(startprint,ghost+7)+term.on_color_rgb(r,g,b)+term.black+'•'+str(Players[player]['ghostsLocationList'][ghost][0])+'-'+str(Players[player]['ghostsLocationList'][ghost][1])+':'+str(Players[player]['ghosts'][Players[player]['ghostsLocationList'][ghost]])+'%'+term.normal+term.move_xy(190,190),end='',flush=True)

def IsItAdjacent(currtuple,futuple):#CHARLIE
    """Check if the current and futur location or the target are adjacent
   Parameters
   ----------
   currtuple: list with the coordinates of the current location of the ghost(str)
   futuple: list with coordinates of the futur location of the ghost(str)
   returns
   -------
   True: when the locations or target are adjacent
   False: when the locations or the target aren't adjacent"""
    if (futuple[0] == (currtuple[0] + 1)) and ((futuple[1] ==currtuple[1]) or (futuple[1] ==(currtuple[1] +1)) or (futuple[1] == (currtuple[1] -1))):
        return True
    elif (futuple[0] == (currtuple[0]-1)) and ((futuple[1]==currtuple[1]) or (futuple[1] ==(currtuple[1] +1)) or (futuple[1] == (currtuple[1] -1))):
        return True
    elif (futuple[0] == currtuple[0]) and ((futuple[1] == (currtuple[1] +1)) or (futuple[1] == (currtuple[1] -1))):
        return True
    else:
        return False
    
def isCaseFree(Players,futuple):#CHARLIE
   """checks if the future location of the ghost is free
   Parameters
   ----------
   futuple: list of coordinates of the future location of the ghost(str)
   Players: main dictionary
   Returns
   ------
   free: the location is free or not"""
   free=True
   allghostsLocation= Players[1]["ghostsLocationList"] + Players[2]["ghostsLocationList"]
   allPlayersPopLocation= [Players[1]["ghostPopLocation"], Players[2]["ghostPopLocation"]]   
   if futuple in allghostsLocation or futuple in allPlayersPopLocation:
      free = False
   return free

def moveGhost(Players,PlayerID,currtuple,futuple,ghostsdone,movementflag):#HABIB
   """Moves the ghost to another location
   Parameters
   ----------
   currtuple: list with the coordinates of the current location of the ghost(str)
   futuple: list with coordinates of the futur location of the ghost(str)
   Returns
   ------
   PLayers: main dictionary"""
   if currtuple in Players[PlayerID]["ghostsLocationList"]and currtuple not in ghostsdone and isCaseFree(Players,futuple) == True and IsItAdjacent(currtuple,futuple) == True:
      movementflag = True
      holdHealth=Players[PlayerID]["ghosts"][currtuple]
      del Players[PlayerID]["ghosts"][currtuple]
      Players[PlayerID]["ghosts"][futuple]=holdHealth
      ghostsdone.append(futuple)
      for i in range(len(Players[PlayerID]["ghostsLocationList"])):
         if Players[PlayerID]["ghostsLocationList"][i] == currtuple:
            k=i
      del Players[PlayerID]["ghostsLocationList"][k]
      Players[PlayerID]["ghostsLocationList"].append(futuple)
      moveVisual(Players,PlayerID,currtuple,futuple)   
   return movementflag

def getOrderslist(MapXY,type_1,type_2, Players,MagicDict,MagicList):#HABIB
    """Takes orders from players and stock them in a list
    Parameters
    ----------
    orderslistP1P2: empty dictionary
    Returns
    -------
    orderslistP1P2: dictionary with a list of the orders from the players"""
    orderslistP1P2=[]
    if type_1 == type_2 and type_1 == "human":
      for player in [1,2]:
        if player == 1 :
          print(term.normal+term.move_xy(0,MapXY[1]+5)+"Player " + str(player) + " Insert your orders : "+str(type_1)+term.move_xy(0,MapXY[1]+6)+term.clear_eol+term.red3,end='',flush=True)
          orders=input()
        else:
          print(term.normal+term.move_xy(27+MapXY[1]*2,MapXY[1]+5)+"Player " + str(player) + " Insert your orders : "+str(type_2)+term.normal+term.move_xy(27+MapXY[1]*2,MapXY[1]+6)+term.clear_eol+term.blue3,end='',flush=True)
          orders=input()
        print(term.normal)
        orderslistP1P2.append(orders.split())    
      return orderslistP1P2
    elif type_1 == type_2 and type_1 == "AI" :
       for player in [1,2]:
        if player == 1 :
          print(term.normal+term.move_xy(0,MapXY[1]+5)+"Player " + str(player) + " Insert your orders : "+str(type_1)+term.move_xy(0,MapXY[1]+6)+term.clear_eol+term.red3,end='',flush=True)
          orders=aiOrders(Players,player,MapXY,MagicDict,MagicList)
        else:
          print(term.normal+term.move_xy(27+MapXY[1]*2,MapXY[1]+5)+"Player " + str(player) + " Insert your orders : "+str(type_2)+term.normal+term.move_xy(27+MapXY[1]*2,MapXY[1]+6)+term.clear_eol+term.blue3,end='',flush=True)
          orders=aiOrders(Players,player,MapXY,MagicDict,MagicList)
        print(term.normal)
        orderslistP1P2.append(orders.split())    
       return orderslistP1P2
    elif  type_1 == "human" and type_2 == "AI":
       for player in [1,2]:
        if player == 1 :
          print(term.normal+term.move_xy(0,MapXY[1]+5)+"Player " + str(player) + " Insert your orders : "+str(type_1)+term.move_xy(0,MapXY[1]+6)+term.clear_eol+term.red3,end='',flush=True)
          orders=input()
        else:
          print(term.normal+term.move_xy(27+MapXY[1]*2,MapXY[1]+5)+"Player " + str(player) + " Insert your orders : "+str(type_2)+term.normal+term.move_xy(27+MapXY[1]*2,MapXY[1]+6)+term.clear_eol+term.blue3,end='',flush=True)
          orders=aiOrders(Players,player,MapXY,MagicDict,MagicList)
        print(term.normal)
        orderslistP1P2.append(orders.split())    
       return orderslistP1P2
    elif  type_1 == "AI" and type_2 == "human":
       for player in [1,2]:
        if player == 1 :
          print(term.normal+term.move_xy(0,MapXY[1]+5)+"Player " + str(player) + " Insert your orders : "+str(type_1)+term.move_xy(0,MapXY[1]+6)+term.clear_eol+term.red3,end='',flush=True)
          orders=aiOrders(Players,player,MapXY,MagicDict,MagicList)
        else:
          print(term.normal+term.move_xy(27+MapXY[1]*2,MapXY[1]+5)+"Player " + str(player) + " Insert your orders :"+str(type_2)+term.normal+term.move_xy(27+MapXY[1]*2,MapXY[1]+6)+term.clear_eol+term.blue3,end='',flush=True)
          orders=input()
        print(term.normal)
        orderslistP1P2.append(orders.split())    
       return orderslistP1P2 
      
def Invokeghost (Players,PlayerID,ghostsdone):#LINA 
    """Invoke a new ghost
    Parameters
    ----------
    Players: a dictionary
    PlayersID: ID of the players in the dictionary"""
    if Players[PlayerID]["magic"] >= 300 and (not(Players[PlayerID]["ghostPopLocation"] in Players[PlayerID]["ghostsLocationList"])):
        Players[PlayerID]["magic"] -= 300
        Players[PlayerID]["ghostsLocationList"].append((Players[PlayerID]["ghostPopLocation"][0],Players[PlayerID]["ghostPopLocation"][1]))
        Players[PlayerID]["ghosts"][(Players[PlayerID]["ghostPopLocation"][0],Players[PlayerID]["ghostPopLocation"][1])] = 100
        ghostsdone.append((Players[PlayerID]["ghostPopLocation"][0],Players[PlayerID]["ghostPopLocation"][1]))
        if PlayerID == 1:
          print(term.move_xy(25+Players[PlayerID]['ghostPopLocation'][0]*2,Players[PlayerID]['ghostPopLocation'][1])+term.on_blue+'😇'+term.normal+term.move_xy(50,50),end ='',flush=True)
        else:
          print(term.move_xy(25+Players[PlayerID]['ghostPopLocation'][0]*2,Players[PlayerID]['ghostPopLocation'][1])+term.on_blue+'👺'+term.normal+term.move_xy(50,50),end ='',flush=True)
    return Players

def updateMagicDisplay(Players,MapXY):#CHARLIE
   """Updates the magicpoints of each player on the display"""
   print(term.move_xy(11,2)+term.on_color_rgb(173,173,223)+"     "+term.move_xy(11,2)+str(Players[1]['magic'])+term.move_xy(70,70),end='',flush=True)
   print(term.move_xy(25+MapXY[0]*2+10,2)+term.on_color_rgb(223,173,223)+"     "+term.move_xy(25+MapXY[0]*2+10,2)+str(Players[2]['magic'])+term.move_xy(70,70),end='',flush=True)

def updateGhostsNumberDisplay(Players,MapXY):#CHARLIE
   """Updates the number of the amount of ghost each player has"""
   print(term.move_xy(11,4)+term.on_color_rgb(173,173,223)+str(len(Players[1]['ghostsLocationList']))+term.normal+term.move_xy(70,70),end='',flush=True)
   print(term.move_xy(25+MapXY[0]*2+10,4)+term.on_color_rgb(223,173,223)+str(len(Players[2]['ghostsLocationList']))+term.normal+term.move_xy(70,70),end='',flush=True)             

def Healghost(Players,PlayerID,targetGhost,amount,ghostsdone):#CHARLIE
    """Heal ghost with chosen amount and reduce twice the amount from magic"""
    if targetGhost in Players[PlayerID]["ghostsLocationList"] and Players[PlayerID]["magic"] >= (amount*2) and (Players[PlayerID]["ghosts"][targetGhost] + amount <= 100) and (targetGhost not in ghostsdone) :
       Players[PlayerID]["ghosts"][targetGhost] += amount
       Players[PlayerID]["magic"] -= (amount*2)
       ghostsdone.append(targetGhost)
    return Players

def transformOrder (splitted):#CHARLIE
    """Transforms the orders of the player into a list
    splitted: the orders of the player"""
    firsthalflist=splitted[0].split("-")
    firstTuple=(int(firsthalflist[0]),int(firsthalflist[1]))
    lol = splitted[1][0+1:]
    secondHalfList=lol.split("-")
    secondTuple=(int(secondHalfList[0]),int(secondHalfList[1]))
    fulltuple= [firstTuple,secondTuple]
    return fulltuple 

def deletefromMagiclist(case,MagicList):#LINA 
     """deletes the coordinates of the case with magic from magiclist
    Parameters
    ----------
    case: coordinates of the location of the case with magic 
    Returns
    -------  
    MagicList: Empty list
 """  
     iid=-1
     for k in range(len(MagicList)):
        if MagicList[k] == case:
           iid=k
     if iid != -1 :
       del MagicList[iid]
     return MagicList

def deletefromghostlist(case,Players):#LINA 
   """deletes coordinates of the ghost from ghostList
   Parameters
   ----------
   case: coordinates of the location of the ghost   
   Players: Main dictionary"""
   for i in [0,1]:
     iid=-1
     for k in range(len(Players[i+1]["ghostsLocationList"])):
        if Players[i+1]["ghostsLocationList"][k] == case:
           iid=k
     if iid != -1 :
       del Players[i+1]["ghostsLocationList"][iid]

def grantMagic(Players,PlayerID,from_to,MagicList,MagicDict,ghostsdone):#LINA 
   """Add points of magic of the case collected by the player to the player
   Parameters
   ----------
   Players: Main dictionary
   PlayersID: ID of the players in the dictionary
   from_to: coordinates of the location of the ghost 
   MagicList: Empty list
   MagicDict: Empty dictionary
   ghostsdone: list des ghost qui ont deja exucuter une action"""
   if from_to in MagicList:
      Players[PlayerID]["magic"] += MagicDict[from_to]
      ghostsdone.append(from_to)
      del MagicDict[from_to]
      deletefromMagiclist(from_to,MagicList)


def transformOrderForGathering(splitted):#CHARLIE
    """Divides the orders into parts
    Parameter
    ---------
    splitted: list of orders from the player
    Returns
    -------
    firsttuple: list with the first part of the orders"""

    firsthalflist=splitted[0].split("-")
    firstTuple=(int(firsthalflist[0]),int(firsthalflist[1]))   
    return firstTuple

def transformOrderForHeals (splitted):#CHARLIE
    """Transforms orders for the function Heal
    Returns
    -------
    fulltuple: list of orders for the function Heal"""
    firsthalflist=splitted[0].split("-")
    firstTuple=(int(firsthalflist[0]),int(firsthalflist[1]))
    lol = splitted[1][0+1:]
    secondHalfList=lol.split("-")
    AmountTuple=(int(secondHalfList[0]))
    fulltuple= [firstTuple,AmountTuple]
    return fulltuple 

def cleanOrders(list):#HABIB
  """Checks the function of the orders and puts them in a list"""
  newlist=[[],[]]
  for i in [0,1]:
    if "ghost" in list[i] :
     newlist[i].append("ghost")  
    for order in list[i]:
        if ":+" in order:
          halfSplit=order.split(":+")
          if len(halfSplit)== 2 and  halfSplit[1].isdigit():
             if "-" in halfSplit[0]:
                testXY=halfSplit[0].split("-")
                if len(testXY) == 2 and testXY[0].isdigit() and testXY[1].isdigit():
                   newlist[i].append(str(order))
        elif ":$" in order:
          halfSplit=order.split(":$")
          if len(halfSplit) == 2 and halfSplit[0] != "" and halfSplit[1] == "":
             if "-" in halfSplit[0]:
                testXY=halfSplit[0].split("-")
                if len(testXY) == 2 and testXY[0].isdigit() and testXY[1].isdigit():
                  newlist[i].append(str(order))
        elif ":@" in order:
           halfSplit=order.split(":@")
           if len(halfSplit) == 2 and halfSplit[0]!="" and halfSplit[1]!="":
             if "-" in halfSplit[0] and "-" in halfSplit[1] :
                testXY1=halfSplit[0].split("-")
                testXY2=halfSplit[1].split("-")
                if len(testXY1) == 2 and testXY1[0].isdigit() and testXY1[1].isdigit() and len(testXY2) == 2 and testXY2[0].isdigit() and testXY2[1].isdigit():
                  newlist[i].append(str(order))       
        elif ":x" in order:
           halfSplit=order.split(":x")
           if len(halfSplit) == 2 and halfSplit[0]!="" and halfSplit[1]!="":
             if "-" in halfSplit[0] and "-" in halfSplit[1] :
                testXY1=halfSplit[0].split("-")
                testXY2=halfSplit[1].split("-")
                if len(testXY1) == 2 and testXY1[0].isdigit() and testXY1[1].isdigit() and len(testXY2) == 2 and testXY2[0].isdigit() and testXY2[1].isdigit():
                  newlist[i].append(str(order))        
  return newlist

def updateemoji(Players):#LINA
   """Updats the emoji of the ghost"""
   for i in [0,1]:  
     for case in Players[i+1]["ghostsLocationList"]:
        print(term.move_xy(25+case[0]*2,case[1])+term.on_blue+returnCorrectGhostEmoji(i,case,Players[i+1]["ghosts"][case])+term.normal+term.move_xy(50,50),end ='',flush=True)  

def moveVisual(Players,PlayerID,currtuple,futuple):#CHARLIE
   """adds the original color of the case back and moves the emoji of the ghost to the correct case"""
   if (currtuple[0]+currtuple[1])%2 ==0 :
     print(term.move_xy(25+currtuple[0]*2,currtuple[1])+term.on_color_rgb(44,95,45)+'  '+term.normal+term.move_xy(50,50),end ='',flush=True)
   else:
     print(term.move_xy(25+currtuple[0]*2,currtuple[1])+term.on_color_rgb(173,223,173)+'  '+term.normal+term.move_xy(50,50),end ='',flush=True)
   print(term.move_xy(25+futuple[0]*2,futuple[1])+term.on_blue+returnCorrectGhostEmoji(PlayerID-1,futuple,Players[PlayerID]["ghosts"][futuple])+term.normal+term.move_xy(50,50),end ='',flush=True)
   return  None

def reEstablishCase(Players,MapXY,case,MagicDict,MagicList):#HABIB
   """adds the original color of the case back"""
   if case in MagicList:
      if (case[0]+case[1])%2 == 0 :
            print(term.move_xy(25+case[0]*2,case[1])+term.on_color_rgb(44,95,45)+returnCorrectMagicEmoji(MagicDict[case])+term.normal+term.move_xy(50,50),end='',flush=True)
      else :
            print(term.move_xy(25+case[0]*2,case[1])+term.on_color_rgb(173,223,173)+returnCorrectMagicEmoji(MagicDict[case])+term.normal+term.move_xy(50,50),end='',flush=True)
   elif (case[0]+case[1])%2 == 0 :
       print(term.move_xy(25+case[0]*2,case[1])+term.on_color_rgb(44,95,45)+'  '+term.normal+term.move_xy(50,50),end='',flush=True)
   else:
       print(term.move_xy(25+case[0]*2,case[1])+term.on_color_rgb(173,223,173)+'  '+term.normal+term.move_xy(50,50),end='',flush=True) 
   
def Phase1(Correctorrders,Players,MapXY,ghostsdone):#LINA
     """Phase one of game: Invokes a ghost and updates the display"""
     for i in [0,1]:
       if 'ghost' in Correctorrders[i]:
         Invokeghost(Players,i+1,ghostsdone)
         
         updateMagicDisplay(Players,MapXY)
         updateGhostsNumberDisplay(Players,MapXY)
         updateGhostsPannel(Players,MapXY)
         del Correctorrders[i][0]

def Phase2(Correctorrders,Players,MapXY,ghostsdone):#CHARLIE
     """Phase two of the game: Heals the ghost and updates the display"""
     for i in [0,1]:
      for order in Correctorrders[i]:
        splitted=order.split(':')
        if splitted[1][0] == "+" :
          from_to=transformOrderForHeals(splitted)
          thisghost = from_to[0]
          amount=from_to[1]
          Healghost(Players,i+1,thisghost,amount,ghostsdone) 
          updateMagicDisplay(Players,MapXY)
          updateGhostsPannel(Players,MapXY)
          updateemoji(Players)  

def Phase3(Correctorrders,Players,MapXY,MagicList,MagicDict,ghostsdone):#HABIB
     """Phase tree of the game: Collects the magic and updates the display"""
     for i in [0,1]:
      for order in Correctorrders[i]:
        splitted=order.split(':')
        if splitted[1][0] == "$" :
          from_to=transformOrderForGathering(splitted)
          grantMagic(Players,i+1,from_to,MagicList,MagicDict,ghostsdone)  
          updateMagicDisplay(Players,MapXY)
          
          
def Phase4(Correctorrders,Players,MapXY,ghostsdone,MagicDict,MagicList,deathflag):#HABIB
     """Phase four of the magic: Attacks ghost and updates the display"""
     P1P2attackOrders=[]
     for i in [0,1]:
      for order in Correctorrders[i]:
        splitted=order.split(':')
        if splitted[1][0] == "x" :
          from_to=transformOrder(splitted)
          fromhere = from_to[0]
          tohere=from_to[1]
          if i == 0:
             check=2
          else:
             check = 1
          if IsItAdjacent(fromhere,tohere) == True and (tohere in Players[check]["ghostsLocationList"] ):
             Players[i+1]["magic"] += 10
             ghostsdone.append(fromhere)
             updateMagicDisplay(Players,MapXY)
             P1P2attackOrders.append(tohere)   
     for k in [0,1]:
               for case in P1P2attackOrders:
                 if case in Players[k+1]["ghostsLocationList"]:
                    
                    Players[k+1]["ghosts"][case] -= 10
                    if Players[k+1]["ghosts"][case] <= 0:
                      deathflag = True
                      updateGhostsPannel(Players,MapXY)
                      deletefromghostlist(case,Players)
                      reEstablishCase(Players,MapXY,case
                                      ,MagicDict,MagicList)
                      del Players[k+1]["ghosts"][case]
                 updateMagicDisplay(Players,MapXY)
                 updateGhostsPannel(Players,MapXY)
                 updateGhostsNumberDisplay(Players,MapXY)     
def Phase5(Correctorrders,Players,MapXY,ghostsdone,MagicDict,MagicList,movementflag):#CHARLIE
     """Phase five of the game: Moves the ghost and updates the display"""
     for i in [0,1]:
      for order in Correctorrders[i]:
        movementflag == False
        splitted=order.split(':')
        if splitted[1][0] == "@" :
          from_to=transformOrder(splitted)
          fromhere = from_to[0]
          tohere=from_to[1]
          if tohere[0] <= MapXY[0] and tohere[0] > 0 and tohere[1] <= MapXY[1] and tohere[1] > 0 : 
            dd = moveGhost(Players,i+1,fromhere,tohere,ghostsdone,movementflag)
            if dd == True :
              reEstablishCase(Players,MapXY,fromhere,MagicDict,MagicList)
              updateGhostsNumberDisplay(Players,MapXY)
              updateGhostsPannel(Players,MapXY)          
def Phase6(Players,MapXY):#NATAN
     """Add points of magic for each player at the end of every round
      Parameters
      ----------
      Players: A dictionary
      MapXY: Empty dictionary
      """
     for i in [1,2]:
        Players[i]["magic"] +=  10
     updateMagicDisplay(Players,MapXY)

def aiOrders(Players,PlayerID,MapXY,MagicDict,MagicList):#HABIB
    """Orders of the AI"""
    aiOrdersString =""                             
   #GHOST BUYING DECISION
    if Players[PlayerID]["ghostPopLocation"] in Players[PlayerID]["ghostsLocationList"] :
       createOrders = str(Players[PlayerID]["ghostPopLocation"][0])+"-"+str(Players[PlayerID]["ghostPopLocation"][1])+":@"+ str(Players[PlayerID]["ghostPopLocation"][0]+random.randint(-1,1))+"-"+str(Players[PlayerID]["ghostPopLocation"][1]+random.randint(-1,1))+" "
       aiOrdersString += createOrders
    if Players[PlayerID]["magic"] >= 30:
       createOrders = "ghost "
       aiOrdersString+= createOrders
    for ghost in Players[PlayerID]["ghostsLocationList"]:
       if ghost in MagicList:
          createOrders = str(ghost[0])+"-"+str(ghost[1])+":$"
          aiOrdersString+= createOrders
       elif PlayerID == 1 :
         createOrders = str(ghost[0])+"-"+str(ghost[1])+":@"+ str(ghost[0]+random.randint(0,1))+"-"+str(ghost[1]+random.randint(0,1))+" "
         aiOrdersString+= createOrders
       else :
         createOrders = str(ghost[0])+"-"+str(ghost[1])+":@"+ str(ghost[0]+random.randint(-1,0))+"-"+str(ghost[1]+random.randint(-1,0))+" "
         aiOrdersString+= createOrders

    time.sleep(0.1)
    return aiOrdersString


def displayScoreGhostZero(Players,MapXY):#LINA
   """Decides the winning player after who's ghosts will end first 
   Parameters
   ----------
   Players: A dictionary
   MapXY: Empty dictionary
   """
   print(term.home+term.clear)
   if len(Players[2]["ghostsLocationList"]) == 0 and len(Players[1]["ghostsLocationList"]) == 0 : 
     print("####    𝔻R𝔸𝕎    ####") 
   elif len(Players[1]["ghostsLocationList"]) == 0 :
     print(term.move_xy(round(term.width/3),round(term.height/3)),"𝕋H𝔼 𝕎𝕀NN𝔼R 𝕀𝕊 :P𝕃𝔸𝕐𝔼R 𝕋𝕎𝕆  🧛  \n" + term.move_xy(round(10),round(term.height/2))+str(len(Players[1]["ghostsLocationList"]))+"  -  " +str(len(Players[2]["ghostsLocationList"]))+term.normal+term.move_xy(50,50),end ='',flush=True)
   else :
      print(term.move_xy(round(term.width/3),round(term.height/3)),"𝕋H𝔼 𝕎𝕀NN𝔼R 𝕀𝕊 : P𝕃𝔸𝕐𝔼R 𝕆N𝔼  🧝   \n" +term.move_xy(round(10),round(term.height/2))+ str(len(Players[2]["ghostsLocationList"]))+"  -  " +str(len(Players[1]["ghostsLocationList"]))+term.normal+term.move_xy(50,50),end ='',flush=True)

def displayScore(Players,MapXY):#LINA
   """Decide the wining player from the point of magic of each player after having 200 round without a win
   Parameters
   ----------
   Players: A dictionary
   MapXY: Empty dictionary
   """
   print(term.home+term.clear)
   if Players[1]["magic"] > Players[2]["magic"] : 
     print(term.move_xy(round(term.width/3),round(term.height/3)),"𝕋H𝔼 𝕎𝕀NN𝔼R 𝕀𝕊 : P𝕃𝔸𝕐𝔼R 𝕆N𝔼  🧝  \n" + term.move_xy(round(10),round(term.height/2))+str(Players[1]["score"])+"  -  " +str(Players[2]["score"])+term.normal+term.move_xy(50,50),end ='',flush=True)
   elif Players[1]["magic"] < Players[2]["magic"] :
     print(term.move_xy(round(term.width/3),round(term.height/3)),"𝕋H𝔼 𝕎𝕀NN𝔼R 𝕀𝕊 : P𝕃𝔸𝕐𝔼R 𝕋𝕎𝕆  🧛  \n" +term.move_xy(round(10),round(term.height/2))+ str(Players[2]["score"])+"  -  " +str(Players[1]["score"])+term.normal+term.move_xy(50,50),end ='',flush=True)
   else :
      print("####    𝔻R𝔸𝕎    ####")
   print(term.move_xy(round(12),round(term.height/5))+ str(Players[1]["magic"])+"  -  " +str(Players[2]["magic"])+term.normal+term.move_xy(50,50),end ='',flush=True)
    
def playgame(map_path, group_1, type_1, group_2, type_2):
  """Plays the entire course of the game"""
  print(term.home+term.clear)
  tourcounter = 0
  ghostsdone=[]
  movementflag = False
  game_over=False
  deathflag=False
#Initialise Players dictionary
  Players = {
    1 : {"ghostPopLocation":() ,"ghosts": {},"ghostsLocationList": [],"magic": 500,"score" : 0,},
    2 : {"ghostPopLocation": () ,"ghosts": {},"ghostsLocationList": [],"magic": 500,"score" : 0}}
#Initialise  Maplist
  MapXY=initialiseMapXY(map_path)  
#Initialise MagicDict and Magiclist
  MagicDict = getMagicDict(map_path)
  MagicList=getMagicList(map_path)
  setInitialGhostsAndPopSpot(Players,getLines(map_path))
  printBoards(MapXY,MagicList,MagicDict,Players)
  updateGhostsPannel(Players,MapXY)
  while game_over == False:
    tourcounter += 1
    Initorders = getOrderslist(MapXY,type_1,type_2, Players,MagicDict,MagicList)
    Correctorrders = cleanOrders(Initorders)

     #GHOST BUYING PHASE
    Phase1(Correctorrders,Players,MapXY,ghostsdone)
    #GHOST HEALING PHASE
    Phase2(Correctorrders,Players,MapXY,ghostsdone)
    #GHOST GATHERING PHASE
    Phase3(Correctorrders,Players,MapXY,MagicList,MagicDict,ghostsdone)
    #GHOST ATTACK PHASE
    Phase4(Correctorrders,Players,MapXY,ghostsdone,deathflag,MagicDict,deathflag)
    #CHECK IF ANY PLAYER HAS 0 GHOSTS
    if (len(Players[1]["ghostsLocationList"])) == 0 or (len(Players[2]["ghostsLocationList"])) == 0 :
      displayScoreGhostZero(Players,MapXY)
      game_over = True
    #GHOST MOVEMENT PHASE
    Phase5(Correctorrders,Players,MapXY,ghostsdone,MagicDict,MagicList,movementflag)
    #POINT REGENERATION
    Phase6(Players,MapXY)
    if tourcounter == 200 and deathflag == False :
       print(term.home+term.clear)
       displayScore(Players,MapXY)
       game_over = True
    ghostsdone=[] 
#-------------------------------------------------------------------------------------------------------------------
  


playgame("Map.txt","groupe1","human","groupe2","human")

