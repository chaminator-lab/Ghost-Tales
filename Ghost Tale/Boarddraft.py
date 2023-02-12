import random
rows=22
colls=22
Players = {
    1 : {
        "ghost": {},
        "magic": 500,
    },
    2 : {
        "ghost": {},
        "magic": 500,
    }
}
fh = open("Map.txt", "r")
lines = fh.readlines()
ghost1 = lines[3].split()
ghost2 = lines[4].split()
Players[1]["ghost"] =  [[int(ghost1[1]), (int(ghost1[2]))],100]
Players[2]["ghost"] = [[int(ghost2[1]), (int(ghost2[2]))], 100]
print(Players[1]["ghost"][0])
CELLS=[[row,col]for row in range(rows) for col in range(colls)]
def createBoardDict(rows,colls,Players):
    
    for cell in CELLS:
        if cell[0] in (0,rows-1) or cell[1] in (0,colls-1):
            print(u'🌲', end='') 
        elif cell == Players[1]["ghost"][0]:
            print(u'👺',end='')  
        elif cell == Players[2]["ghost"][0]:
            print(u'😇',end='')          
        elif (cell[1]+cell[0])%10.5 == 0:
            print(u'🟦' ,end ='')
        elif cell in [[17,12],[10,8],[7,5]]:
            print(u'🌯' ,end ='') 
        else :
            x= random.randint(0,1)
            if x == 0:
                print(u'🟩' ,end ='')
            else:
                print(u'🟫' ,end ='')
             
        if cell[1] == colls-1:
            print('')
        #if cell [0] == 2 and cell[1] == 2:
            #print('🟪' ,end ='')

createBoardDict(rows,colls,Players)


BOARD = {(1,1):{'ghost': True,'food': 100 }}
FOOD={(1,2): 100,2:500}
lisst = [[0,1],[2,3],[5,6]]
hold=0
print('EVIL Ghosts          ⚔         Namur Heroes')
print (u'💀🧛',u'\💉 ',0,u'\🩸 ',500,end='')
print(' |',500,u'🔮/ ',0,u'🧹/ ' '' u'🧙‍♂️🎓',end='')




