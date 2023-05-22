from src.headers import *

# importing classes
from src.board import Boardofgame
from src.buildings import *
from src.back import Background
from src.king import *
from src.input import *
from src.examples import *
from src.queen import *
from src.all import *
# from src.hit import sathvika1
obj_get1 = Get()
def walldamage(listindex, hurtx, hurty,damage):
    # print("j")
    obj_walls[listindex].hitss(damage)
    if obj_walls[listindex].hitpoints > 50 and obj_walls[listindex].hitpoints < 100:
        obj_walls[listindex].shape = [[WALL1]]
        obj_walls[listindex].show(
            obj_board.grid, obj_walls[listindex].shape, hurtx, hurty)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_walls[listindex].hitpoints < 50 and obj_walls[listindex].hitpoints > 20:
        obj_walls[listindex].shape = [[WALL2]]
        obj_walls[listindex].show(
            obj_board.grid, obj_walls[listindex].shape, hurtx, hurty)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
    elif obj_walls[listindex].hitpoints < 20 and obj_walls[listindex].hitpoints > 0:
        obj_walls[listindex].shape = [[WALL3]]
        obj_walls[listindex].show(
            obj_board.grid, obj_walls[listindex].shape, hurtx, hurty)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_walls[listindex].hitpoints <= 0:
        # obj_hurt[listindex].shape=[[HURT1]]
        # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
        obj_board.grid[hurtx][hurty] = BACK
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
        obj_example.decrease()
        # print(game)
        # obj_hurt[listindex].setx(0)
        obj_walls[listindex]._live = 0


def townhitpoint(x1,y1,damage):
    obj_town.hitss(damage)
    if obj_town.hitpoints > 50 and obj_town.hitpoints < 100:
        obj_town.shape = [[CH1, CH1, CH1], [
            CH1, CH1, CH1], [CH1, CH1, CH1], [CH1, CH1, CH1]]
        obj_town.show(
            obj_board.grid, obj_town.shape, val1town, val2town)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    if obj_town.hitpoints > 20 and obj_town.hitpoints < 50:
        obj_town.shape = [[CH2, CH2, CH2], [
            CH2, CH2, CH2], [CH2, CH2, CH2], [CH2, CH2, CH2]]
        obj_town.show(
            obj_board.grid, obj_town.shape, val1town, val2town)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
    if obj_town.hitpoints > 0 and obj_town.hitpoints < 20:
        obj_town.shape = [[CH3, CH3, CH3], [
            CH3, CH3, CH3], [CH3, CH3, CH3], [CH3, CH3, CH3]]
        obj_town.show(
            obj_board.grid, obj_town.shape, val1town, val2town)
        os.system('clear')
        obj_board.print_board(2)
        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_town.hitpoints <= 0:
        # obj_hurt[listindex].shape=[[HURT1]]
        # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
        for x in range(x1, x1+4):
            for y in range(y1, y1+3):
                obj_board.grid[x][y] = BACK

        obj_town._live=0
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
        obj_example.decrease()


def sprs(listindex, hurtx, hurty,damage):
    # print("j")
    obj_hurt[listindex].hitss(damage)
    if obj_hurt[listindex].hitpoints > 50 and obj_hurt[listindex].hitpoints < 100:
        obj_hurt[listindex].shape = [[HURT1]]
        obj_hurt[listindex].show(
            obj_board.grid, obj_hurt[listindex].shape, hurtx, hurty)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_hurt[listindex].hitpoints < 50 and obj_hurt[listindex].hitpoints > 20:
        obj_hurt[listindex].shape = [[HURT2]]
        obj_hurt[listindex].show(
            obj_board.grid, obj_hurt[listindex].shape, hurtx, hurty)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
    elif obj_hurt[listindex].hitpoints < 20 and obj_hurt[listindex].hitpoints > 0:
        obj_hurt[listindex].shape = [[HURT3]]
        obj_hurt[listindex].show(
            obj_board.grid, obj_hurt[listindex].shape, hurtx, hurty)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_hurt[listindex].hitpoints <= 0:
        # obj_hurt[listindex].shape=[[HURT1]]
        # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
        obj_board.grid[hurtx][hurty] = BACK
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
        obj_example.decrease()
        # print(game)
        # obj_hurt[listindex].setx(0)
        obj_hurt[listindex]._live = 0


# obj_archer=[]

def samhitha(damage):
    obj_town.hitss(damage)
    if obj_town.hitpoints > 50 and obj_town.hitpoints < 100:
        obj_town.shape = [[CH1, CH1, CH1], [
            CH1, CH1, CH1], [CH1, CH1, CH1], [CH1, CH1, CH1]]
        obj_town.show(
            obj_board.grid, obj_town.shape, val1town, val2town)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    if obj_town.hitpoints > 20 and obj_town.hitpoints < 50:
        obj_town.shape = [[CH2, CH2, CH2], [
            CH2, CH2, CH2], [CH2, CH2, CH2], [CH2, CH2, CH2]]
        obj_town.show(
            obj_board.grid, obj_town.shape, val1town,val2town )
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
    if obj_town.hitpoints > 0 and obj_town.hitpoints < 20:
        obj_town.shape = [[CH3, CH3, CH3], [
            CH3, CH3, CH3], [CH3, CH3, CH3], [CH3, CH3, CH3]]
        obj_town.show(
            obj_board.grid, obj_town.shape, val1town, val2town)
        os.system('clear')
        obj_board.print_board(2)
        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_town.hitpoints <= 0:
        # obj_hurt[listindex].shape=[[HURT1]]
        # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
        for x in range(val1town, val1town+4):
            for y in range(val2town, val2town+3):
                obj_board.grid[x][y] = BACK
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
        obj_example.decrease()


def sathvika(listindex, hurtx, hurty):
    # print("j")
    obj_hurt[listindex].hitpoint()
    if obj_hurt[listindex].hitpoints > 50 and obj_hurt[listindex].hitpoints < 100:
        obj_hurt[listindex].shape = [[HURT1]]
        obj_hurt[listindex].show(
            obj_board.grid, obj_hurt[listindex].shape, hurtx, hurty)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_hurt[listindex].hitpoints < 50 and obj_hurt[listindex].hitpoints > 20:
        obj_hurt[listindex].shape = [[HURT2]]
        obj_hurt[listindex].show(
            obj_board.grid, obj_hurt[listindex].shape, hurtx, hurty)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
    elif obj_hurt[listindex].hitpoints < 20 and obj_hurt[listindex].hitpoints > 0:
        obj_hurt[listindex].shape = [[HURT3]]
        obj_hurt[listindex].show(
            obj_board.grid, obj_hurt[listindex].shape, hurtx, hurty)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_hurt[listindex].hitpoints <= 0:
        # obj_hurt[listindex].shape=[[HURT1]]
        # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
        obj_board.grid[hurtx][hurty] = BACK
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
        obj_example.decrease()
        # print(game)
        # obj_hurt[listindex].setx(0)
        obj_hurt[listindex]._live = 0

def cannonhealth3(list, x1, y1,damage):
    # print("c")
    obj_cannon[list].hitss(damage)
    print(obj_cannon[list].hitpoints)
    if obj_cannon[list].hitpoints > 50 and obj_cannon[list].hitpoints < 100:
        # print("in")
        obj_cannon[list].shape = [[CH1, CH1, CH1], [
            CH1, CH1, CH1], [CH1, CH1, CH1]]
        obj_cannon[list].show(
            obj_board.grid, obj_cannon[list].shape, x1, y1)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    if obj_cannon[list].hitpoints > 20 and obj_cannon[list].hitpoints < 50:
        obj_cannon[list].shape = [[CH2, CH2, CH2], [
            CH2, CH2, CH2], [CH2, CH2, CH2]]
        obj_cannon[list].show(
            obj_board.grid, obj_cannon[list].shape, x1, y1)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
    if obj_cannon[list].hitpoints > 0 and obj_cannon[list].hitpoints < 20:
        obj_cannon[list].shape = [[CH3, CH3, CH3], [
            CH3, CH3, CH3], [CH3, CH3, CH3]]
        obj_cannon[list].show(
            obj_board.grid, obj_cannon[list].shape, x1, y1)
        os.system('clear')
        obj_board.print_board(2)
        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_cannon[list].hitpoints <= 0:
        # obj_hurt[listindex].shape=[[HURT1]]
        # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
        for x in range(x1, x1+3):
            for y in range(y1, y1+3):
                obj_board.grid[x][y] = BACK
        obj_cannon[list]._live = 0
        os.system('clear')
        # obj_cannon[list]._live=0
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
        obj_example.decrease()

def wizardhitpoints(list,x1,y1,damage):
    obj_wizard[list].hitss(damage)
    print(obj_wizard[list].hitpoints)
    if obj_wizard[list].hitpoints > 50 and obj_wizard[list].hitpoints < 100:
        # print("in")
        obj_wizard[list].shape = [[CH1, CH1, CH1], [
            CH1, CH1, CH1], [CH1, CH1, CH1]]
        obj_wizard[list].show(
            obj_board.grid, obj_wizard[list].shape, x1, y1)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    if obj_wizard[list].hitpoints > 20 and obj_wizard[list].hitpoints < 50:
        obj_wizard[list].shape = [[CH2, CH2, CH2], [
            CH2, CH2, CH2], [CH2, CH2, CH2]]
        obj_wizard[list].show(
            obj_board.grid, obj_wizard[list].shape, x1, y1)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
    if obj_wizard[list].hitpoints > 0 and obj_wizard[list].hitpoints < 20:
        obj_wizard[list].shape = [[CH3, CH3, CH3], [
            CH3, CH3, CH3], [CH3, CH3, CH3]]
        obj_wizard[list].show(
            obj_board.grid, obj_wizard[list].shape, x1, y1)
        os.system('clear')
        obj_board.print_board(2)
        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_wizard[list].hitpoints <= 0:
        # obj_hurt[listindex].shape=[[HURT1]]
        # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
        for x in range(x1, x1+3):
            for y in range(y1, y1+3):
                obj_board.grid[x][y] = BACK
        obj_wizard[list]._live = 0
        os.system('clear')
        # obj_wizard[list]._live=0
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
        obj_example.decrease()





def queenmove():
    # print("in")
    # print("ff")
    global directionq
    char = input_to(obj_get1, 0.08)
    if char == 'W':
        directionq = 0
        obj_queen.queen_clear(obj_board.grid)
        speed1 = obj_queen.getspeed()
        if obj_queen.getx_p()-speed1>0 and obj_queen.getx_p()-speed1<HEIGHT and obj_board.grid[obj_queen.getx_p()-speed1][obj_queen.gety_p()]==BACK: 
           obj_queen.setx_p(obj_queen.getx_p()-speed1)
           obj_queen.queen_move(
           obj_board.grid, obj_queen.getx_p(), obj_queen.gety_p())
           obj_queen.queen_show(
           obj_board.grid, obj_queen.getx_p(), obj_queen.gety_p())
           os.system('clear')
           obj_board.print_board(2)
           total = obj_board.printboard(2)
           new_array.append(total)

    elif char == 'D':
        directionq = 1
        obj_queen.queen_clear(obj_board.grid)
        speed1 = obj_queen.getspeed()
        if obj_queen.gety_p()+speed1 >0 and obj_queen.gety_p()+speed1<WIDTH and obj_board.grid[obj_queen.getx_p()][obj_queen.gety_p()+speed1]==BACK:
           obj_queen.sety_p(obj_queen.gety_p()+speed1)
           obj_queen.queen_move(
           obj_board.grid, obj_queen.getx_p(), obj_queen.gety_p())
           obj_queen.queen_show(
           obj_board.grid, obj_queen.getx_p(), obj_queen.gety_p())
           os.system('clear')
           obj_board.print_board(2)
           total = obj_board.printboard(2)
           new_array.append(total)
    elif char == 'A':
        directionq = 2
        obj_queen.queen_clear(obj_board.grid)
        speed1 = obj_queen.getspeed()
        if obj_queen.gety_p()-speed1>0 and obj_queen.gety_p()-speed1<WIDTH and obj_board.grid[obj_queen.getx_p()][obj_queen.gety_p()-speed1]==BACK:

            obj_queen.sety_p(obj_queen.gety_p()-speed1)
            obj_queen.queen_move(
            obj_board.grid, obj_queen.getx_p(), obj_queen.gety_p())
            obj_queen.queen_show(
            obj_board.grid, obj_queen.getx_p(), obj_queen.gety_p())
            os.system('clear')
            obj_board.print_board(2)
            total = obj_board.printboard(2)
            new_array.append(total)
    elif char == 'S':
        directionq = 3
        obj_queen.queen_clear(obj_board.grid)
        speed1 = obj_queen.getspeed()
        if obj_queen.getx_p()+speed1>0 and obj_queen.getx_p()+speed1<HEIGHT and obj_board.grid[obj_queen.getx_p()+speed1][obj_queen.gety_p()]==BACK:
           obj_queen.setx_p(obj_queen.getx_p()+speed1)
           obj_queen.queen_move(
           obj_board.grid, obj_queen.getx_p(), obj_queen.gety_p())
           obj_queen.queen_show(
            obj_board.grid, obj_queen.getx_p(), obj_queen.gety_p())
           os.system('clear')
           obj_board.print_board(2)
           total = obj_board.printboard(2)
           new_array.append(total)
    elif char == ' ':
        if directionq == 0:
            qx = obj_queen.getx_p()
            qy = obj_queen.gety_p()
            for x in range(qx-10, qx-5):
                for y in range(qy-2, qy+3):
                    for list in range(0, inhou):
                        if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
                            listindex = list
                            sprs(listindex, x, y,obj_queen.damage)
                        elif x == val1town and y == val2town:
                            samhitha(obj_queen.damage)
                    for list in range(0,canno):
                        if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
                            cannonhealth3(list,x,y,obj_queen.damage)
                    for list in range(0,wizard):
                        if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
                            wizardhitpoints(list,x,y,obj_queen.damage)

                    for list in range(0,walls):
                        if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
                            walldamage(list,x,y,obj_queen.damage)
            # if obj_dumx.getx()==1 and time.time()-sathtime>1 and time.time()-sathtime<2:
            #     obj_dumx.setx(0)
            #     for x in range(qx-20, qx-11):
            #         for y in range(qy-4, qy+5):
            #             for list in range(0, inhou):
            #                 if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
            #                     listindex = list
            #                     sprs(listindex, x, y,obj_queen.damage)
            #                 elif x == val1town and y == val2town:
            #                     samhitha(obj_queen.damage)
            #             for list in range(0,canno):
            #                 if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
            #                     cannonhealth3(list,x,y,obj_queen.damage)
            #             for list in range(0,wizard):
            #                  if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
            #                      wizardhitpoints(list,x,y,obj_queen.damage)

            #             for list in range(0,walls):
            #                 if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
            #                     walldamage(list,x,y,obj_queen.damage)



        elif directionq == 1:
            qx = obj_queen.getx_p()
            qy = obj_queen.gety_p()
            for x in range(qx-2, qx+3):
                for y in range(qy+6, qy+11):
                    for list in range(0, inhou):
                        if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
                            listindex = list
                            sprs(listindex, x, y,obj_queen.damage)
                        elif x == val1town and y == val2town:
                            samhitha(obj_queen.damage)

                    for list in range(0,canno):
                        if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
                            cannonhealth3(list,x,y,obj_queen.damage)

                    for list in range(0,wizard):
                        if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
                            wizardhitpoints(list,x,y,obj_queen.damage)
                    for list in range(0,walls):
                        if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
                            walldamage(list,x,y,obj_queen.damage)

            # if obj_dumx.getx()==1 and time.time()-sathtime>1 and time.time()-sathtime<2:
            #     obj_dumx.setx(0)
            #     for x in range(qx-4, qx+5):
            #         for y in range(qy+12, qy+21):
            #             for list in range(0, inhou):
            #                 if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
            #                     listindex = list
            #                     sprs(listindex, x, y,obj_queen.damage)
            #                 elif x == val1town and y == val2town:
            #                     samhitha(obj_queen.damage)
            #             for list in range(0,canno):
            #                 if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
            #                     cannonhealth3(list,x,y,obj_queen.damage)
            #             for list in range(0,wizard):
            #                  if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
            #                      wizardhitpoints(list,x,y,obj_queen.damage)

            #             for list in range(0,walls):
            #                 if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
            #                     walldamage(list,x,y,obj_queen.damage)


        elif directionq == 2:
            qx = obj_queen.getx_p()
            qy = obj_queen.gety_p()
            for x in range(qx-2, qx+3):
                for y in range(qy-10, qy-5):
                    for list in range(0, inhou):
                        if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
                            listindex = list
                            sprs(listindex, x, y,obj_queen.damage)
                        elif x == val1town and y == val2town:
                            samhitha(obj_queen.damage)

                    for list in range(0,canno):
                        if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
                            cannonhealth3(list,x,y,obj_queen.damage)
                    
                    for list in range(0,wizard):
                        if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
                            wizardhitpoints(list,x,y,obj_queen.damage)

                    for list in range(0,walls):
                        if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
                            walldamage(list,x,y,obj_queen.damage)
            # if obj_dumx.getx()==1 and time.time()-sathtime>1 and time.time()-sathtime<2:
            #     obj_dumx.setx(0)
            #     for x in range(qx-4, qx+5):
            #         for y in range(qy-20, qy+11):
            #             for list in range(0, inhou):
            #                 if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
            #                     listindex = list
            #                     sprs(listindex, x, y,obj_queen.damage)
            #                 elif x == val1town and y == val2town:
            #                     samhitha(obj_queen.damage)
            #             for list in range(0,canno):
            #                 if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
            #                     cannonhealth3(list,x,y,obj_queen.damage)
            #             for list in range(0,wizard):
            #                  if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
            #                      wizardhitpoints(list,x,y,obj_queen.damage)

            #             for list in range(0,walls):
            #                 if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
            #                     walldamage(list,x,y,obj_queen.damage)


        elif directionq == 3:
            qx = obj_queen.getx_p()
            qy = obj_queen.gety_p()
            for x in range(qx+6, qx+11):
                for y in range(qy-2, qy+3):
                    for list in range(0, inhou):
                        if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
                            listindex = list
                            sprs(listindex, x, y,obj_queen.damage)
                        elif x == val1town and y == val2town:
                            samhitha(obj_queen.damage)

                    for list in range(0,canno):
                        if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
                            cannonhealth3(list,x,y,obj_queen.damage)

                    for list in range(0,wizard):
                        if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
                            wizardhitpoints(list,x,y,obj_queen.damage)
                    
                    for list in range(0,walls):
                        if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
                            walldamage(list,x,y,obj_queen.damage)

            # if obj_dumx.getx()==1 and time.time()-sathtime>1 and time.time()-sathtime<2:
            #     obj_dumx.setx(0)
            #     for x in range(qx+12, qx+21):
            #         for y in range(qy-4, qy+5):
            #             for list in range(0, inhou):
            #                 if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
            #                     listindex = list
            #                     sprs(listindex, x, y,obj_queen.damage)
            #                 elif x == val1town and y == val2town:
            #                     samhitha(obj_queen.damage)
            #             for list in range(0,canno):
            #                 if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
            #                     cannonhealth3(list,x,y,obj_queen.damage)
            #             for list in range(0,wizard):
            #                  if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
            #                      wizardhitpoints(list,x,y,obj_queen.damage)

            #             for list in range(0,walls):
            #                 if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
            #                     walldamage(list,x,y,obj_queen.damage)


def queenxtra():
    qx = obj_queen.getx_p()
    qy = obj_queen.gety_p()
    if obj_dumx.getx()==1 and time.time()-sathtime>1 and time.time()-sathtime<2 and directionq==0:
        obj_dumx.setx(0)
        for x in range(qx-20, qx-11):
            for y in range(qy-4, qy+5):
                for list in range(0, inhou):
                    if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
                        listindex = list
                        sprs(listindex, x, y,obj_queen.damage)
                    elif x == val1town and y == val2town:
                        samhitha(obj_queen.damage)
                for list in range(0,canno):
                    if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
                        cannonhealth3(list,x,y,obj_queen.damage)
                for list in range(0,wizard):
                    if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
                        wizardhitpoints(list,x,y,obj_queen.damage)

                for list in range(0,walls):
                    if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
                        walldamage(list,x,y,obj_queen.damage)

    if obj_dumx.getx()==1 and time.time()-sathtime>1 and time.time()-sathtime<2 and directionq==1:
        obj_dumx.setx(0)
        for x in range(qx-4, qx+5):
            for y in range(qy+12, qy+21):
                for list in range(0, inhou):
                    if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
                        listindex = list
                        sprs(listindex, x, y,obj_queen.damage)
                    elif x == val1town and y == val2town:
                        samhitha(obj_queen.damage)
                for list in range(0,canno):
                    if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
                        cannonhealth3(list,x,y,obj_queen.damage)
                for list in range(0,wizard):
                    if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
                        wizardhitpoints(list,x,y,obj_queen.damage)

                for list in range(0,walls):
                    if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
                        walldamage(list,x,y,obj_queen.damage)

    if obj_dumx.getx()==1 and time.time()-sathtime>1 and time.time()-sathtime<2 and directionq==2:
        obj_dumx.setx(0)
        for x in range(qx-4, qx+5):
            for y in range(qy-20, qy-10):
                for list in range(0, inhou):
                    if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
                        listindex = list
                        sprs(listindex, x, y,obj_queen.damage)
                    elif x == val1town and y == val2town:
                        samhitha(obj_queen.damage)
                for list in range(0,canno):
                    if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
                        cannonhealth3(list,x,y,obj_queen.damage)
                for list in range(0,wizard):
                    if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
                        wizardhitpoints(list,x,y,obj_queen.damage)

                for list in range(0,walls):
                    if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
                        walldamage(list,x,y,obj_queen.damage)

    if obj_dumx.getx()==1 and time.time()-sathtime>1 and time.time()-sathtime<2 and directionq==3:
        obj_dumx.setx(0)
        for x in range(qx+12, qx+21):
            for y in range(qy-4, qy+5):
                for list in range(0, inhou):
                    if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
                        listindex = list
                        sprs(listindex, x, y,obj_queen.damage)
                    elif x == val1town and y == val2town:
                        samhitha(obj_queen.damage)
                for list in range(0,canno):
                    if x==obj_cannon[list]._x and y==obj_cannon[list]._y and obj_cannon[list]._live==1:
                        cannonhealth3(list,x,y,obj_queen.damage)
                for list in range(0,wizard):
                    if x==obj_wizard[list]._x and y==obj_wizard[list]._y and obj_wizard[list]._live==1:
                        wizardhitpoints(list,x,y,obj_queen.damage)

                for list in range(0,walls):
                    if x==obj_walls[list]._x and y==obj_walls[list]._y and obj_walls[list]._live==1:
                        walldamage(list,x,y,obj_queen.damage)


def queenhitpoints(x,y,damage):
    obj_queen.changehealth(damage)
    print(obj_queen.health)
    if obj_queen.health > 50 and obj_queen.health < 100:
        obj_queen.nan = QUE1
        obj_queen.queen_clear(obj_board.grid)
        obj_queen.queen_show(
            obj_board.grid,obj_queen.getx_p(),obj_queen.gety_p())
        # obj_board.grid[x][y]=QUE1
        os.system('clear')
        obj_board.print_board(2)
        # for x in range(0,obj_queen.health):
        #   obj_board.grid[2][x]=HEALTH
        # os.system('clear')
        # obj_board.print_board(2)
        

        total = obj_board.printboard(2)
        new_array.append(total)

    if obj_queen.health > 20 and obj_queen.health < 50:
        obj_queen.nan = QUE2
        obj_queen.queen_show(
            obj_board.grid,x,y)
        # obj_board.grid[x][y]=QUE2
        # os.system('clear')
        # obj_board.print_board(2)
        # for x in range(0,obj_queen.health):
        #   obj_board.grid[2][x]=HEALTH
        os.system('clear')
        obj_board.print_board(2)
        

        total = obj_board.printboard(2)
        new_array.append(total)
    if obj_queen.health > 0 and obj_queen.health < 20:
        obj_queen.nan = QUE3
        obj_queen.queen_show(
            obj_board.grid, x,y)
        # obj_board.grid[x][y]=QUE3
        os.system('clear')
        obj_board.print_board(2)
        # for x in range(0,obj_queen.health):
        #   obj_board.grid[2][x]=HEALTH
        # os.system('clear')
        # obj_board.print_board(2)
        
        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_queen.health <= 0:
        # obj_hurt[listindex].shape=[[HURT1]]
        # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
       
        obj_board.grid[x][y] = BACK
        os.system('clear')
        obj_board.print_board(2)
        # for x in range(0,obj_queen.health):
        #   obj_board.grid[2][x]=HEALTH
        # os.system('clear')
        # obj_board.print_board(2)
        

        total = obj_board.printboard(2)
        new_array.append(total)
        obj_example.decrease()

    



hit_time=time.time()
# hit_time=-1
def canattack():
    # global present_time
    global hit_time
    present_time=time.time()

    # print("")
    for list in range(0, canno):

        # print("jj")
        # print(list)
        #x == obj_cannon[list]._x
       # y == obj_cannon[list]._y
        # print(obj_cannon[list]._x)
        # print(obj_queen.health)
        # print(obj_queen.getx_p())
        for o in range(obj_cannon[list]._x-5, obj_cannon[list]._x+6):
            # print(o)
            # print(obj_queen.getx_p())
            for p in range(obj_cannon[list]._y-5, obj_cannon[list]._y+6):
                # print(o)
                # print(obj_queen.getx_p())

                if  o>0 and o<HEIGHT and p>0 and p<WIDTH and o == obj_queen.getx_p() and p == obj_queen.gety_p() and obj_queen._live == 1 and obj_cannon[list]._live==1 and present_time-hit_time>2:
                    hit_time=time.time()
                    #    print("j")
                    # obj_queen.changehealth(obj_cannon[list]._damage)
                    queenhitpoints(o,p,obj_cannon[list]._damage)
                    # print("in")
                    # obj_queen.health=obj_queen.health-obj_cannon[list]._damage
                    if obj_queen.health <= 0:
                        # queenhitpoints(o,p,obj_cannon[list]._damage)
                        obj_queen._live = 0
                        # obj_board.grid[o][p] = BACK
                        # os.system('clear')
                        # obj_board.print_board(2)

                        # total = obj_board.printboard(2)
                        # new_array.append(total)

                for list in range(0,obj_dum.getx()):
                    # present_time=time.time()
                    # print(o,p)
                    # print(p)
                    if o == obj_archer[list].getx_p() and  p == obj_archer[list].gety_p():
                        print(o,p)
                        print("jj")
                    if  o>0 and o<HEIGHT and p>0 and p<WIDTH and o == obj_archer[list].getx_p() and p == obj_archer[list].gety_p() and obj_archer[list]._live == 1 and obj_cannon[list]._live==1  :
                      print("iii")
                      hit_time=time.time()
                      obj_board.grid[o][p] = BACK
                      obj_archer[list]._live=0


def wizardattack():
    # print("")
    for list in range(0, wizard):

        # print("jj")
        # print(list)
        #x == obj_wizard[list]._x
       # y == obj_wizard[list]._y
        # print(obj_wizard[list]._x)
        # print(obj_queen.health)
        # print(obj_queen.getx_p())
        for o in range(obj_wizard[list]._x-5, obj_wizard[list]._x+6):
            # print(o)
            # print(obj_queen.getx_p())
            for p in range(obj_wizard[list]._y-5, obj_wizard[list]._y+6):
                # print(o)
                # print(obj_queen.getx_p())

                if o == obj_queen.getx_p() and p == obj_queen.gety_p() and obj_queen.live == 1:
                    #    print("j")
                    obj_queen.changehealth(obj_wizard[list]._damage)
                #    obj_queen.health=obj_queen.health-obj_wizard[list]._damage
                    if obj_queen.health <= 0:
                        obj_queen.live = 0
                        obj_board.grid[o][p] = BACK
                        os.system('clear')
                        obj_board.print_board(2)

                        total = obj_board.printboard(2)
                        new_array.append(total)

def canattack1():

    # print("")
    for list in range(0, canno):
        if obj_cannon[list]._live == 1:
            for o in range(obj_cannon[list]._x-5, obj_cannon[list]._x+6):
                # print(o)
                # print(obj_queen.getx_p())
                for p in range(obj_cannon[list]._y-5, obj_cannon[list]._y+6):
                    # print(o)
                    # print(obj_queen.getx_p())

                    if o == obj_king.getx_p() and p == obj_king.gety_p() and obj_king.live == 1:
                        #    print("j")
                        obj_king.changehealth(obj_cannon[list]._damage)
                #    obj_queen.health=obj_queen.health-obj_cannon[list]._damage
                        if obj_king.health <= 0:
                            obj_king.live = 0
                            for x1 in range(o, o+3):
                                for y1 in range(p, p+3):
                                    obj_board.grid[x1][y1] = BACK
                    #    obj_board.grid[o][p]=BACK
                            os.system('clear')
                            obj_board.print_board(2)

                            total = obj_board.printboard(2)
                            new_array.append(total)

                    # for

                    # obj_troop.setvalue(0)
                    # obj_board.grid[o][p]=BACK
                        # obj_troop.setvalue(0)

        # print("jj")
        # print(list)
        #x == obj_cannon[list]._x
        #y == obj_cannon[list]._y
        # print(obj_cannon[list]._x)
        # print(obj_queen.health)
        # print(obj_queen.getx_p())

# obj_archer=[]
# obj_very=very()

def wizardattack1():

    # print("")
    for list in range(0, wizard):
        if obj_wizard[list]._live == 1:
            for o in range(obj_wizard[list]._x-5, obj_wizard[list]._x+6):
                # print(o)
                # print(obj_queen.getx_p())
                for p in range(obj_wizard[list]._y-5, obj_wizard[list]._y+6):
                    # print(o)
                    # print(obj_queen.getx_p())

                    if o == obj_king.getx_p() and p == obj_king.gety_p() and obj_king.live == 1:
                        #    print("j")
                        obj_king.changehealth(obj_wizard[list]._damage)
                #    obj_queen.health=obj_queen.health-obj_wizard[list]._damage
                        if obj_king.health <= 0:
                            obj_king.live = 0
                            for x1 in range(o, o+3):
                                for y1 in range(p, p+3):
                                    obj_board.grid[x1][y1] = BACK
                    #    obj_board.grid[o][p]=BACK
                            os.system('clear')
                            obj_board.print_board(2)

                            total = obj_board.printboard(2)
                            new_array.append(total)


def rupa1():

    print("DD")
    # bool2=bool
    char = input_to(obj_get, 0.08)
    if char == 'L':
        vl1 = random.randint(0, HEIGHT-5)
        vl2 = random.randint(0, WIDTH-10)
        while obj_board.grid[vl1][vl2] != BACK:
            vl1 = random.randint(0, HEIGHT-5)
            vl2 = random.randint(0, WIDTH-10)
        #    sam=1
        # val1 = random.randint(0, HEIGHT-5)
        # val2 = random.randint(0, WIDTH-10)
        # while obj_board.grid[val1][val2] != BACK:
        #     val1 = random.randint(0, HEIGHT-5)
        #     val2 = random.randint(0, WIDTH-10)
        # # obj_king.king_clear(obj_board.grid)

        # obj_troop = troop(val1, val2)
        # obj_very.setx(1)
        obj_archer = Archer(vl1, vl2)
        obj_archer.Archer_show(obj_board.grid, vl1, vl2)
        # print("s")
        obj_archer.setvalue(1)
        # tropid=tropid+1

        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)


xballo1 = random.randint(0, HEIGHT-5)
yballo1 = random.randint(0, WIDTH-10)
while obj_board.grid[xballo1][yballo1] != BACK:
    xballo1 = random.randint(0, HEIGHT-5)
    yballo1 = random.randint(0, WIDTH-10)

obj_ballo1 = []
obj_dum4 = dum()


def spwan1():
    # global obj_troop
    # global obj_troop1
    # global obj_troop2
    # print("ss")

    char = input_to(obj_get, 0.08)
    if char == 'B':
        #    sam=1
        # val1 = random.randint(0, HEIGHT-5)
        # val2 = random.randint(0, WIDTH-10)
        # while obj_board.grid[val1][val2] != BACK:
        #     val1 = random.randint(0, HEIGHT-5)
        #     val2 = random.randint(0, WIDTH-10)
        # # obj_king.king_clear(obj_board.grid)

        # obj_troop = troop(val1, val2)
        obj_ballo1.append(Ballon(xballo1, yballo1))
        obj_ballo1[obj_dum4.getx()].Ballon_show(obj_board.grid, val1, val2)
        obj_ballo1[obj_dum4.getx()].setvalue(1)
        obj_dum4.setx(1)

        # tropid=tropid+1

        os.system('clear')
        obj_board.print_board(2)
        total = obj_board.printboard(2)
        new_array.append(total)


def cannonhealth(list, x1, y1):
    # print("c")
    obj_cannon[list].hitpoint()
    print(obj_cannon[list].hitpoints)
    if obj_cannon[list].hitpoints > 50 and obj_cannon[list].hitpoints < 100:
        # print("in")
        obj_cannon[list].shape = [[CH1, CH1, CH1], [
            CH1, CH1, CH1], [CH1, CH1, CH1]]
        obj_cannon[list].show(
            obj_board.grid, obj_cannon[list].shape, x1, y1)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    if obj_cannon[list].hitpoints > 20 and obj_cannon[list].hitpoints < 50:
        obj_cannon[list].shape = [[CH2, CH2, CH2], [
            CH2, CH2, CH2], [CH2, CH2, CH2]]
        obj_cannon[list].show(
            obj_board.grid, obj_cannon[list].shape, x1, y1)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
    if obj_cannon[list].hitpoints > 0 and obj_cannon[list].hitpoints < 20:
        obj_cannon[list].shape = [[CH3, CH3, CH3], [
            CH3, CH3, CH3], [CH3, CH3, CH3]]
        obj_cannon[list].show(
            obj_board.grid, obj_cannon[list].shape, x1, y1)
        os.system('clear')
        obj_board.print_board(2)
        total = obj_board.printboard(2)
        new_array.append(total)

    elif obj_cannon[list].hitpoints <= 0:
        # obj_hurt[listindex].shape=[[HURT1]]
        # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
        for x in range(x1, x1+3):
            for y in range(y1, y1+3):
                obj_board.grid[x][y] = BACK
        obj_cannon[list]._live = 0
        os.system('clear')
        # obj_cannon[list]._live=0
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
        obj_example.decrease()


obj_dum5 = dum()


def ballon_move1(dd):
    # print("b")
    # print("h")
    x = obj_ballo1[dd].getx_p()
    y = obj_ballo1[dd].gety_p()
    # print(y)
    finalx = x
    finaly = y
    min = 10000
    sos = 0
    print(canno)
    for list in range(0, canno):
        if(obj_cannon[list]._live == 1):
            sos = 1
            spr1 = obj_cannon[list].getx()
            spr2 = obj_cannon[list].gety()
            dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
            if min > dist:
                min = dist

                finalx = spr1
                finaly = spr2

    # if sos==0:
    #     for list in range(0, inhou):
    #         if(obj_hurt[list]._live == 1):
    #            spr1 = obj_hurt[list].getx()
    #            spr2 = obj_hurt[list].gety()
    #            dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
    #            if min > dist:
    #               min = dist

    #               finalx = spr1
    #               finaly = spr2

    #     if obj_town._live==1:
    #        dist = ((((x - val1town)**2) + ((y-val2town)**2))**0.5)
    #        if min > dist:
    #           min = dist

    #           finalx = val1town
    #           finaly = val2town

        # else :
            # print("in")

    # print(finalx)
    obj_ballo1[dd].finalx(finalx)
    obj_ballo1[dd].finaly(finaly)
    # print(finalx)
    # print(finaly)
    movex = 0
    movey = 0
    # r=obj_troop.setreturn()
    # print(r)
    if(obj_ballo1[dd].setreturn() == 1 and sos == 1):
        # print("s")
        x = obj_ballo1[dd].getx_p()
        y = obj_ballo1[dd].gety_p()
        fy = obj_ballo1[dd].getfy()
        fx = obj_ballo1[dd].getfx()
        # # print(y)
        # finalx = x
        # finaly = y
        # min = 10000
        # for list in range(0, inhou):
        #     spr1 = obj_hurt[list].getx()
        #     spr2 = obj_hurt[list].gety()
        #     dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
        #     if min > dist:
        #         min = dist
        #         # print(min)
        #         finalx = spr1
        #         finaly = spr2
        # # print(finalx)
        # print(finaly)
        mindis = 10000
        movex = 0
        movey = 0
        move1x = 0
        move1y = 0
        cos = 0
        ass1 = 0

        # for p in range(-1, 2):
        #     for s in range(-1, 2):
        for list1 in range(0, canno):
            if obj_cannon[list1]._live == 1:
                ass1 = 1
                if x == obj_cannon[list1].getx() and y == obj_cannon[list1].gety():

                    move1x = x
                    move1y = y
                    cos = 1
                    obj_cannon[list1]._live = 0

        # for o in range(x-7,x+8):
        #     # print(o)
        #     # print(obj_queen.getx_p())
        #     for p in range(y-7,y+8):
        #         # print(o)
        #         # print(obj_queen.getx_p())
        #         for list in range(0,inhou):
        #             if o==obj_hurt[list]._x and p==obj_hurt[list]._y:
        #                 sathvi(list,o,p)

        #         if o==val1town and p==val2town:
        #             townhitpoints(val1town,val2town)

        # print(cos)
        if cos == 0:
            ssss = BACK
            # print("s")

            if x-1 > 0:
                dist1 = ((((x-1 - fx)**2) + ((y-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y

            if x+1 < HEIGHT:
                dist1 = ((((x+1 - fx)**2) + ((y-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y

            if y+1 < WIDTH:
                dist1 = ((((x - fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x
                    movey = y+1

            if y-1 > 0:
                dist1 = ((((x - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x
                    movey = y-1

            if x-1 > 0 and y-1 > 0:
                dist1 = ((((x-1 - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y-1

            if x+1 < HEIGHT and y+1 < WIDTH:
                dist1 = ((((x+1 - fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y+1

            if y+1 < WIDTH and x-1 > 0:
                dist1 = ((((x-1 - fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y+1

            if y-1 > 0 and x+1 < HEIGHT:
                dist1 = ((((x+1 - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y-1

            if obj_ballo1[dd].start == 0:
                obj_ballo1[dd].lastx(movex)
                obj_ballo1[dd].lasty(movey)
                obj_ballo1[dd].sss = obj_board.grid[movex][movey]
                obj_ballo1[dd].start = 1
            else:
                ssss = obj_board.grid[movex][movey]

            # print("s")
            # for p in range(-1, 2):
            #     for s in range(-1, 2):
            #         if obj_board.grid[x+p][y+s] == BACK or obj_board.grid[x+p][y+s]==WALL:
            #             if p == 0 and s == 0:

            #                sath = 1
            #             else:
            #                 dist1 = ((((x+p - fx)**2) + ((y+s-fy)**2))**0.5)
            #                 if(mindis > dist1):
            #                    mindis = dist1
            #                    movex = x+p
            #                    movey = y+s
                # dist1=((((p - finalx )**2) + ((s-finaly)**2) )**0.5)
                # if( mindis >dist1):
                #     mindis=dist1
                #     movex=p
                #     movey=s

        # print(movex)
        # print(movey)
            obj_ballo1[dd].Ballon_clear(obj_board.grid)

            obj_ballo1[dd].Ballon_move(obj_board.grid, movex, movey)
            obj_ballo1[dd].sety_p(movey)
            obj_ballo1[dd].setx_p(movex)
            obj_ballo1[dd].Ballon_show(obj_board.grid, movex, movey)
            os.system('clear')
            obj_board.print_board(2)
            if obj_ballo1[dd].start == 1:
                # obj_ballo1[dd].lastx(movex)
                # obj_ballo1[dd].lasty(movey)
                # obj_ballo1[dd].sss=obj_board.grid[movex][movey]
                # obj_ballo1[dd].start=1

                obj_board.grid[x][y] = obj_ballo1[dd].sss
                os.system('clear')
                obj_board.print_board(2)
                obj_ballo1[dd].lastx(movex)
                obj_ballo1[dd].lasty(movey)
                obj_ballo1[dd].sss = ssss
        else:
            for list in range(0, canno):
                # print("s")
                if move1x == obj_cannon[list].getx() and move1y == obj_cannon[list].gety():
                    # global Attime
                    # Attime=time.time()

                    # obj_board.grid[move1x][move1y] = BACK
                    # print("ss")
                    SS = 0
                    while obj_cannon[list].hitpoints >= 0:
                        global stime
                        stime = time.time()
                        SS = SS+1
                        # if(Attime-stime>0.0005):
                        if SS % 10 == 0:
                            cannonhealth(list, move1x, move1y)
                            obj_ballo1[dd].sss = BACK
                        #   Attime=stime
                        # else :
                        #     # time.sleep(0.5)

                        #     sathvi(list,move1x,move1y)
                        #   Attime=stime

                    # obj_hurt[list]._live = 0
                    cos = 0

    if obj_ballo1[dd].setreturn() == 1 and sos == 0:
        # obj_ballo1[dd].start = 0
        sam = 0
        sam1=0
        for list in range(0, inhou):
            if(obj_hurt[list]._live == 1):
                sam = 1
                spr1 = obj_hurt[list].getx()
                spr2 = obj_hurt[list].gety()
                dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
                if min > dist:
                    min = dist

                    finalx = spr1
                    finaly = spr2

        if obj_town._live == 1:
            sam1 = 1
            dist = ((((x - val1town)**2) + ((y-val2town)**2))**0.5)
            if min > dist:
                min = dist

                finalx = val1town
                finaly = val2town

        obj_ballo1[dd].finalx(finalx)
        obj_ballo1[dd].finaly(finaly)
    # print(finalx)
    # print(finaly)
        movex = 0
        movey = 0
        # if sam==0:
        #     obj_board.grid[x][y]=Fore.GREEN + Back.BLACK + Style.BRIGHT +"B"+ Style.RESET_ALL
        if sam==0:
            obj_board.grid[x][y]=Fore.GREEN + Back.BLACK + Style.BRIGHT +"B"+ Style.RESET_ALL
        if sam == 1 or sam1==1:
            x = obj_ballo1[dd].getx_p()
            y = obj_ballo1[dd].gety_p()
            fy = obj_ballo1[dd].getfy()
            fx = obj_ballo1[dd].getfx()
            mindis = 10000
            movex = 0
            movey = 0
            move1x = 0
            move1y = 0
            cos = 0

            # for p in range(-1, 2):
            #     for s in range(-1, 2):
            # if x > 0 and x < HEIGHT and y > 0 and y < WIDTH and obj_board.grid[x][y] == HURT:
                        # cos=1
                # move1x = x
                # move1y = y
            for list in range(0, inhou):

                            # print("s")
                if x == obj_hurt[list]._x and y == obj_hurt[list]._y and obj_hurt[list]._live == 1:
                        # obj_board.grid[move1x][move1y] = BACK
                        move1x = x
                        move1y = y
                        obj_hurt[list]._live = 0
                        cos = 1

            if x > 0 and x< HEIGHT and y > 0 and y < WIDTH and x==val1town and y==val2town and obj_town._live==1:
                cos = 1
                obj_town._live=0
                move1x = x
                move1y = y
                

            if cos == 0:
                ssss = BACK
            # print("s")

                if x-1 > 0:
                    dist1 = ((((x-1 - fx)**2) + ((y-fy)**2))**0.5)
                    if(mindis > dist1):
                        mindis = dist1
                        movex = x-1
                        movey = y

                if x+1 < HEIGHT:
                    dist1 = ((((x+1 - fx)**2) + ((y-fy)**2))**0.5)
                    if(mindis > dist1):
                        mindis = dist1
                        movex = x+1
                        movey = y

                if y+1 < WIDTH:
                    dist1 = ((((x - fx)**2) + ((y+1-fy)**2))**0.5)
                    if(mindis > dist1):
                        mindis = dist1
                        movex = x
                        movey = y+1

                if y-1 > 0:
                    dist1 = ((((x - fx)**2) + ((y-1-fy)**2))**0.5)
                    if(mindis > dist1):
                        mindis = dist1
                        movex = x
                        movey = y-1

                if x-1 > 0 and y-1 > 0:
                    dist1 = ((((x-1 - fx)**2) + ((y-1-fy)**2))**0.5)
                    if(mindis > dist1):
                        mindis = dist1
                        movex = x-1
                        movey = y-1

                if x+1 < HEIGHT and y+1 < WIDTH:
                    dist1 = ((((x+1 - fx)**2) + ((y+1-fy)**2))**0.5)
                    if(mindis > dist1):
                        mindis = dist1
                        movex = x+1
                        movey = y+1

                if y+1 < WIDTH and x-1 > 0:
                    dist1 = ((((x-1 - fx)**2) + ((y+1-fy)**2))**0.5)
                    if(mindis > dist1):
                        mindis = dist1
                        movex = x-1
                        movey = y+1

                if y-1 > 0 and x+1 < HEIGHT:
                    dist1 = ((((x+1 - fx)**2) + ((y-1-fy)**2))**0.5)
                    if(mindis > dist1):
                        mindis = dist1
                        movex = x+1
                        movey = y-1

                if obj_ballo1[dd].start == 0:
                    obj_ballo1[dd].lastx(movex)
                    obj_ballo1[dd].lasty(movey)
                    obj_ballo1[dd].sss = obj_board.grid[movex][movey]
                    obj_ballo1[dd].start = 1
                else:
                    ssss = obj_board.grid[movex][movey]

            # print("s")
            # for p in range(-1, 2):
            #     for s in range(-1, 2):
            #         if obj_board.grid[x+p][y+s] == BACK or obj_board.grid[x+p][y+s]==WALL:
            #             if p == 0 and s == 0:

            #                sath = 1
            #             else:
            #                 dist1 = ((((x+p - fx)**2) + ((y+s-fy)**2))**0.5)
            #                 if(mindis > dist1):
            #                    mindis = dist1
            #                    movex = x+p
            #                    movey = y+s
                # dist1=((((p - finalx )**2) + ((s-finaly)**2) )**0.5)
                # if( mindis >dist1):
                #     mindis=dist1
                #     movex=p
                #     movey=s

        # print(movex)
        # print(movey)
                obj_ballo1[dd].Ballon_clear(obj_board.grid)

                obj_ballo1[dd].Ballon_move(obj_board.grid, movex, movey)
                obj_ballo1[dd].sety_p(movey)
                obj_ballo1[dd].setx_p(movex)
                obj_ballo1[dd].Ballon_show(obj_board.grid, movex, movey)
                os.system('clear')
                obj_board.print_board(2)
                if obj_ballo1[dd].start == 1:
                # obj_ballo1[dd].lastx(movex)
                # obj_ballo1[dd].lasty(movey)
                # obj_ballo1[dd].sss=obj_board.grid[movex][movey]
                # obj_ballo1[dd].start=1

                   obj_board.grid[x][y] = obj_ballo1[dd].sss
                   os.system('clear')
                   obj_board.print_board(2)
                   obj_ballo1[dd].lastx(movex)
                   obj_ballo1[dd].lasty(movey)
                   obj_ballo1[dd].sss = ssss
            else:
                for list in range(0, inhou):
                # print("s")
                    if move1x == obj_hurt[list]._x and move1y == obj_hurt[list]._y:
                    # global Attime
                    # Attime=time.time()

                    # obj_board.grid[move1x][move1y] = BACK
                    # print("ss")
                        # obj_ballo1[dd].sss = BACK
                        # obj_ballo1[dd].start = 0
                        # obj_ballo1[dd].Ballon_clear(obj_board.grid)

                        # obj_ballo1[dd].Ballon_move(obj_board.grid, move1x, move1y)
                        # obj_ballo1[dd].sety_p(move1y)
                        # obj_ballo1[dd].setx_p(move1x)
                        # obj_ballo1[dd].Ballon_show(obj_board.grid, move1x, move1y)
                        # os.system('clear')
                        # obj_board.print_board(2)
                        # obj_hurt[list]._live=0
                        SS=0
                        # obj_ballo1[dd].sss = BACK
                        while obj_hurt[list].hitpoints >=0:
                        
                            SS=SS+1
                        # # # if(Attime-stime>0.0005):
                            if SS%10==0:
                              sprs(list,move1x,move1y,obj_ballo1[dd].damage)
                              obj_ballo1[dd].sss = BACK
                              obj_ballo1[dd].sety_p(move1y)
                              obj_ballo1[dd].setx_p(move1x)
                        #   Attime=stime
                        # else :
                        #     # time.sleep(0.5)

                        #     sathvi(list,move1x,move1y)
                        #   Attime=stime


                        
                    # obj_hurt[list]._live = 0
                        cos = 0
                if move1x == val1town and move1y == val2town:
                    # obj_ballo1[dd].start = 0
                    
                    # Attime=time.time()

                    # obj_board.grid[move1x][move1y] = BACK
                    # print("ss")
                    SS=0
                    while obj_town.hitpoints >=0:
                        # global stime
                        # stime=time.time()
                        # SS=SS+1
                        # if(Attime-stime>0.0005):
                        if SS%10==0:
                            townhitpoint(move1x,move1y,obj_ballo1[dd].damage)
                            obj_ballo1[dd].sss = BACK
                            obj_ballo1[dd].sety_p(move1y)
                            obj_ballo1[dd].setx_p(move1x)
                        #   Attime=stime
                        #   Attime=stime
                        # else :
                        #     # time.sleep(0.5)

                        #     sathvi(list,move1x,move1y)
                        #   Attime=stime


                        
                    # obj_hurt[list]._live = 0
                    cos = 0

                # print("s")
              
