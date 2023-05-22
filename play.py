from src.headers import *
from src.all import * 
# import time
import json
from src.all1 import *
# print("King to play : 1")
# print("Queen to play : 0")
# head=int(input())
# if head==1:
#     # obj_verify.setx(1)
#     print(obj_verify.getx())
# else :
#     obj_verify.setx(0)
# sath='p'
# for x in range(0,obj_king.health):
#     sath=sath+'p'
# print(sath)
# new_array=[]

obj_board.print_board(2)
total=obj_board.printboard(2)
new_array.append(total)
# print(total)
# obj_troop=[]
# tropid=0
# print(Direction)
# for x in range(0,20):
#     obj_board.grid[2][x+5]=HEALTH
i=0
spr1=6
spr=7
troop1=0

# rupa()
timex=-1
finaldec=0
finals=0
bool=1
levels=1
while bool:
    if obj_queen._live==0:
        finaldec=1
    
    for list in range(0,inhou):
        if obj_hurt[list]._live==1:
            finals=1

    for list in range(0,canno):
        if obj_cannon[list]._live==1:
            finals=1

    for list in range(0,wizard):
        if obj_cannon[list]._live==1:
            finals=1

    if obj_town._live==1:
        finals=1

            
    if finals==0:
        # create()
        bool=0
    finals=0
    if finaldec==1 :
         bool=0
        
    # finaldec=0
    


    
    

    


    
    # if head==1:
    #     sath=HEALTH
    #     for x in range(0,obj_queen.health):
    #       obj_board.grid[2][x]=HEALTH
    #     os.system('clear')
    #     obj_board.print_board(2)
        

    #     #   sath=sath+HEALTH
    #     # print(sath)
        
    time.sleep(0.0010)
   
    hint=0
    ex=1
    for list in range(0,inhou):
        if obj_hurt[list]._live==1 :
           hint=1
    
    # for x in range(0,obj_king.health):
    #     print("s")
    # print(i)

    troopmove()
    for list in range(0,obj_dum.getx()):
    #    if time.time()-timex>0.5:
        archer_move1(list)
        archer_move1(list)
        #  timex=time.time()
    for list in range(0,obj_dum1.getx()):
       archer_move2(list)
       archer_move2(list)
    for list in range(0,obj_dum2.getx()):
       archer_move3(list)
       archer_move3(list)
    for list in range(0,obj_dum4.getx()):
       ballon_move1(list)
    # else :
        
        
    #     for p in range(-1, 2):
    #         for s in range(-1, 2):
    #             if obj_board.grid[obj_troop.getx_p()+p][obj_troop.gety_p()+s] == HURT:
    #                 obj_board.grid[obj_troop.getx_p()+p][obj_troop.gety_p()+s]=BACK

    

    # for x in range (0,6):
    #     if obj_hurt[x].getx()!=0 or obj_hurt[x].gety()!=0:
    #         i=1

    if(obj_example.getx()==0):
        print("game over")
        
    # i=i+1
    
    if head==1:
        kingmove()
        canattack1()
    else :
        # sath='p'
        # for x in range(0,obj_queen.health):
        #     sath=sath+'p'
        #     print(sath)
        if obj_queen._live==1:
           queenmove()
           queenxtra()
        canattack()

    spwan1()
    spwan()
    #rupa()
    

# print(new_array[0]) 
  

with open("replay.json", "r+") as file:

    data = json.load(file)

    data["games"].append(new_array)

    file.seek(0)

    file.close()

with open("replay.json", "w") as file:

    json.dump(data, file)
    file.close()
    



os.system('clear')
print("over")
