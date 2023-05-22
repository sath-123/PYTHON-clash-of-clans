# from turtle import ontimer
from xml.sax.xmlreader import AttributesImpl
from src.headers import *

# importing classes
from src.board import Boardofgame
from src.buildings import *
from src.back import Background
from src.king import *
from src.input import *
from src.examples import *
from src.queen import *


# obj_example = example(7)
# obj_get = Get()

# obj_verify = verify()
# gameover=1



obj_example = example(7)
obj_get = Get()

obj_verify = verify()


obj_board = Boardofgame(HEIGHT, WIDTH)
obj_board.create_board()
# obj_board.create_house()


obj_back = Background()
# obj_back.display_ceil(obj_board.grid)s
obj_back.display_floor(obj_board.grid)
obj_back.display_ceil(obj_board.grid)
# obj_back.create_house(obj_board.grid)
val1town = random.randint(0, HEIGHT-5)
val2town = random.randint(0, WIDTH-10)
while obj_board.grid[val1town][val2town] != BACK:
    val1town = random.randint(0, HEIGHT-5)
    val2town = random.randint(0, WIDTH-10)
    
obj_town = Townhall(val1town, val2town, 100)
obj_town.show(obj_board.grid, obj_town.shape, val1town, val2town)
print("King to play : 1")
print("Queen to play : 0")

head = int(input())
print("level 1 :1")
print("level 2 :2")
print("level 3 :3")
level=int(input())
# print(level)
if level==1:
    ravi=2
    
elif level==2:
    ravi=3
elif level==3:
    ravi=4

print(head)
if(head == 1):
    vaking = random.randint(0, HEIGHT-5)
    vasking = random.randint(0, WIDTH-10)
    # obj_queen = queen(va, vas)
    obj_king = king(vaking, vasking)
    obj_king.king_show(obj_board.grid, vaking, vasking)
    # spr = 16
    # spr1 = 19
    # obj_king.king_move(obj_board.grid, spr, spr1)
elif(head == 0):
    va = random.randint(0, HEIGHT-5)
    vas = random.randint(0, WIDTH-10)
    obj_queen = queen(va, vas)
    obj_queen.queen_show(obj_board.grid, va, vas)
canno = 0
walls=0
obj_cannon = []
obj_walls=[]
while walls<60 :
    val1s1 = random.randint(2, HEIGHT-2)
    val2s1 = random.randint(2, WIDTH-2)
    i = 1
    # print("enter")
    
    if obj_board.grid[val1s1][val2s1] != BACK:
        i = 0
    if(i == 1):
        obj_walls.append(Walls(val1s1, val2s1, 90))
        # print(obj_hurt[inhou].hitpoints)
        obj_walls[walls].show(obj_board.grid, obj_walls[walls].shape,
                             obj_walls[walls].getx(), obj_walls[walls].gety())
        walls = walls+1

while canno < ravi:
    val1s = random.randint(15, HEIGHT-15)
    val2s = random.randint(15, WIDTH-15)
    i = 1
    # print("enter")
    for p in range(val1s, val1s+3):
        for s in range(val2s, val2s+3):
            if obj_board.grid[p][s] != BACK:
                i = 0

    if(i == 1):
        obj_cannon.append(cannon(val1s, val2s, 100))
        # print(obj_hurt[inhou].hitpoints)
        obj_cannon[canno].show(obj_board.grid, obj_cannon[canno].shape,
                               obj_cannon[canno].getx(), obj_cannon[canno].gety())
        canno = canno+1

obj_wizard=[]
wizard=0
while wizard < ravi:
    wizx = random.randint(5, HEIGHT-5)
    wizy = random.randint(5, WIDTH-5)
    i = 1
    # print("enter")
    for p in range(wizx, wizx+3):
        for s in range(wizy, wizy+3):
            if obj_board.grid[p][s] != BACK:
                i = 0

    if(i == 1):
        obj_wizard.append(Wizard(wizx, wizy, 100))
        # print(obj_hurt[inhou].hitpoints)
        obj_wizard[wizard].show(obj_board.grid, obj_wizard[wizard].shape,
                               obj_wizard[wizard].getx(), obj_wizard[wizard].gety())
        wizard = wizard+1


# obj_king = king(6, 9)
# obj_king.king_show(obj_board.grid, 6, 9)
# spr = 16
# spr1 = 19
# obj_king.king_move(obj_board.grid, spr, spr1)
inhou = 0
inhou1 = 10
while inhou < 15:
    val1 = random.randint(0, HEIGHT-5)
    val2 = random.randint(0, WIDTH-10)
    # print(val1)
    # print(val2)
    i = 1
    # print("enter")
    for p in range(val1, val1+4):
        for s in range(val2, val2+3):
            if obj_board.grid[p][s] != BACK:
                i = 0

    if(i == 1):
        obj_hurt.append(Magnet(val1, val2, 90))
        # print(obj_hurt[inhou].hitpoints)
        obj_hurt[inhou].show(obj_board.grid, obj_hurt[inhou].shape,
                             obj_hurt[inhou].getx(), obj_hurt[inhou].gety())
        inhou = inhou+1


def kingmove():
    global Direction
    char = input_to(obj_get, 0.08)
    if char == 'D':
        Direction = 0
        obj_king.king_clear(obj_board.grid)
        speed = obj_king.getspeed()
        obj_king.sety_p(obj_king.gety_p()+speed)
        obj_king.king_move(
            obj_board.grid, obj_king.getx_p(), obj_king.gety_p())
        obj_king.king_show(
            obj_board.grid, obj_king.getx_p(), obj_king.gety_p())
        os.system('clear')
        obj_board.print_board(2)
        total = obj_board.printboard(2)
        new_array.append(total)
    elif char == 'W':
        Direction = 1
        obj_king.king_clear(obj_board.grid)
        speed = obj_king.getspeed()
        obj_king.setx_p(obj_king.getx_p()-speed)
        obj_king.king_move(
            obj_board.grid, obj_king.getx_p(), obj_king.gety_p())
        obj_king.king_show(
            obj_board.grid, obj_king.getx_p(), obj_king.gety_p())
        os.system('clear')
        obj_board.print_board(2)
        total = obj_board.printboard(2)
        new_array.append(total)
    elif char == 'A':
        Direction = 2
        speed = obj_king.getspeed()
        obj_king.king_clear(obj_board.grid)
        obj_king.sety_p(obj_king.gety_p()-speed)
        obj_king.king_move(
            obj_board.grid, obj_king.getx_p(), obj_king.gety_p())
        obj_king.king_show(
            obj_board.grid, obj_king.getx_p(), obj_king.gety_p())
        os.system('clear')
        obj_board.print_board(2)
        total = obj_board.printboard(2)
        new_array.append(total)
    elif char == 'S':
        Direction = 3
        speed = obj_king.getspeed()
        obj_king.king_clear(obj_board.grid)
        obj_king.setx_p(obj_king.getx_p()+speed)
        obj_king.king_move(
            obj_board.grid, obj_king.getx_p(), obj_king.gety_p())
        obj_king.king_show(
            obj_board.grid, obj_king.getx_p(), obj_king.gety_p())
        os.system('clear')
        obj_board.print_board(2)
        total = obj_board.printboard(2)
        new_array.append(total)
    elif char == 'O':
        damage = obj_king.getdamage()*2
        speed = obj_king.getspeed()*2

        obj_king.shells1(damage, speed)
        print(obj_king.getspeed())
    elif char == 'P':
        # damage=obj_king.getdamage()*2
        # speed=obj_king.getspeed()*2

        obj_king.shells()
        # print(obj_king.getspeed())

    elif char == ' ':
        # global hurtx
        # global hurty
        # global listindex
        sathvika = 0
        if(Direction == 2):

            # sathvika = 0
            # obj_king.sety_p(obj_king.gety_p()-1)
            if obj_board.grid[obj_king.getx_p()][obj_king.gety_p()-1] == HURT:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()-1] == HURT:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()-1] == HURT:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()-1] == HURT1:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()-1] == HURT1:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()-1] == HURT1:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()-1] == HURT2:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()-1] == HURT2:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()-1] == HURT2:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()-1

            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()-1] == HURT3:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()-1] == HURT3:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()-1] == HURT3:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()-1] == CH:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()-1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()-1] == CH:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()-1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()-1] == CH:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()-1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()-1] == CH1:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()-1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()-1] == CH1:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()-1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()-1] == CH1:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()-1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()-1] == CH2:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()-1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()-1] == CH2:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()-1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()-1] == CH2:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()-1
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()-1] == CH3:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()-1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()-1] == CH3:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()-1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()-1] == CH3:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()-1
                sathvika = 1

            if sathvika == 0:
                for list in range(0, inhou):
                    if hurtx == obj_hurt[list]._x and hurty == obj_hurt[list]._y:
                        listindex = list
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
                    obj_hurt[listindex].setx(0)
            else:
                obj_town.hitpoint()
                if obj_town.hitpoints > 50 and obj_town.hitpoints < 100:
                    obj_town.shape = [[CH1, CH1, CH1], [
                        CH1, CH1, CH1], [CH1, CH1, CH1], [CH1, CH1, CH1]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)

                if obj_town.hitpoints > 20 and obj_town.hitpoints < 50:
                    obj_town.shape = [[CH2, CH2, CH2], [
                        CH2, CH2, CH2], [CH2, CH2, CH2], [CH2, CH2, CH2]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)

                if obj_town.hitpoints > 0 and obj_town.hitpoints < 20:
                    obj_town.shape = [[CH3, CH3, CH3], [
                        CH3, CH3, CH3], [CH3, CH3, CH3], [CH3, CH3, CH3]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)
                    total = obj_board.printboard(2)
                    new_array.append(total)

                elif obj_town.hitpoints <= 0:
                    # obj_hurt[listindex].shape=[[HURT1]]
                    # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
                    for x in range(20, 24):
                        for y in range(40, 43):
                            obj_board.grid[x][y] = BACK
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)
                    obj_example.decrease()
                    # obj_hurt[listindex].setx(0)

                # gameover=gameover-1

        elif(Direction == 1):
            # obj_king.sety_p(obj_king.gety_p()-1)
            if obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()] == HURT:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+1] == HURT:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+2] == HURT:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+2
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()] == HURT1:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+1] == HURT1:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+2] == HURT1:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+2
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()] == HURT2:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+1] == HURT2:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+2] == HURT2:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+2
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()] == HURT3:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+1] == HURT3:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+2] == HURT3:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+2
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()] == CH:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+1] == CH:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+2] == CH:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+2
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()] == CH1:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+1] == CH1:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+2] == CH1:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+2
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()] == CH2:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+1] == CH2:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+2] == CH2:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+2
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()] == CH3:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+1] == CH3:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()-1][obj_king.gety_p()+2] == CH3:
                hurtx = obj_king.getx_p()-1
                hurty = obj_king.gety_p()+2
                sathvika = 1

            if sathvika == 0:
                for list in range(0, inhou):
                    if hurtx == obj_hurt[list]._x and hurty == obj_hurt[list]._y:
                        listindex = list
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
                    obj_hurt[listindex].setx(0)
                    obj_example.decrease()
            else:
                obj_town.hitpoint()
                if obj_town.hitpoints > 50 and obj_town.hitpoints < 100:
                    obj_town.shape = [[CH1, CH1, CH1], [
                        CH1, CH1, CH1], [CH1, CH1, CH1], [CH1, CH1, CH1]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)

                if obj_town.hitpoints > 20 and obj_town.hitpoints < 50:
                    obj_town.shape = [[CH2, CH2, CH2], [
                        CH2, CH2, CH2], [CH2, CH2, CH2], [CH2, CH2, CH2]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)

                if obj_town.hitpoints > 0 and obj_town.hitpoints < 20:
                    obj_town.shape = [[CH3, CH3, CH3], [
                        CH3, CH3, CH3], [CH3, CH3, CH3], [CH3, CH3, CH3]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)

                elif obj_town.hitpoints <= 0:
                    # obj_hurt[listindex].shape=[[HURT1]]
                    # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
                    for x in range(20, 24):
                        for y in range(40, 43):
                            obj_board.grid[x][y] = BACK
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)
                    obj_example.decrease()
                    # obj_hurt[listindex].setx(0)

        elif(Direction == 3):
            # obj_king.sety_p(obj_king.gety_p()-1)
            if obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()] == HURT:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+1] == HURT:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+2] == HURT:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+2
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()] == HURT1:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+1] == HURT1:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+2] == HURT1:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+2
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()] == HURT2:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+1] == HURT2:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+2] == HURT2:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+2
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()] == HURT3:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+1] == HURT3:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+2] == HURT3:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+2
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()] == CH:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+1] == CH:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+2] == CH:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+2
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()] == CH1:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+1] == CH1:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+2] == CH1:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+2
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()] == CH2:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+1] == CH2:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+2] == CH2:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+2
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()] == CH3:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+1] == CH3:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+1
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+3][obj_king.gety_p()+2] == CH3:
                hurtx = obj_king.getx_p()+3
                hurty = obj_king.gety_p()+2
                sathvika = 1

            if sathvika == 0:
                for list in range(0, inhou):
                    if hurtx == obj_hurt[list]._x and hurty == obj_hurt[list]._y:
                        listindex = list
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
                    obj_hurt[listindex].setx(0)
                    obj_example.decrease()
            else:
                obj_town.hitpoint()
                if obj_town.hitpoints > 50 and obj_town.hitpoints < 100:
                    obj_town.shape = [[CH1, CH1, CH1], [
                        CH1, CH1, CH1], [CH1, CH1, CH1], [CH1, CH1, CH1]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)

                if obj_town.hitpoints > 20 and obj_town.hitpoints < 50:
                    obj_town.shape = [[CH2, CH2, CH2], [
                        CH2, CH2, CH2], [CH2, CH2, CH2], [CH2, CH2, CH2]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)

                if obj_town.hitpoints > 0 and obj_town.hitpoints < 20:
                    obj_town.shape = [[CH3, CH3, CH3], [
                        CH3, CH3, CH3], [CH3, CH3, CH3], [CH3, CH3, CH3]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)

                elif obj_town.hitpoints <= 0:
                    # obj_hurt[listindex].shape=[[HURT1]]
                    # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
                    for x in range(20, 24):
                        for y in range(40, 43):
                            obj_board.grid[x][y] = BACK
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)
                    obj_example.decrease()

        elif(Direction == 0):
            # obj_king.sety_p(obj_king.gety_p()-1)
            if obj_board.grid[obj_king.getx_p()][obj_king.gety_p()+3] == HURT:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()+3] == HURT:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()+3] == HURT:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()+3] == HURT1:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()+3] == HURT1:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()+3] == HURT1:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()+3] == HURT2:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()+3] == HURT2:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()+3] == HURT2:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()+3] == HURT3:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()+3] == HURT3:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()+3] == HURT3:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()+3
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()+3] == CH:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()+3
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()+3] == CH:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()+3
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()+3] == CH:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()+3
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()+3] == CH1:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()+3
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()+3] == CH1:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()+3
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()+3] == CH1:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()+3
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()+3] == CH2:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()+3
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()+3] == CH2:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()+3
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()+3] == CH2:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()+3
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()][obj_king.gety_p()+3] == CH3:
                hurtx = obj_king.getx_p()
                hurty = obj_king.gety_p()+3
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+1][obj_king.gety_p()+3] == CH3:
                hurtx = obj_king.getx_p()+1
                hurty = obj_king.gety_p()+3
                sathvika = 1
            elif obj_board.grid[obj_king.getx_p()+2][obj_king.gety_p()+3] == CH3:
                hurtx = obj_king.getx_p()+2
                hurty = obj_king.gety_p()+3
                sathvika = 1

            if sathvika == 0:
                for list in range(0, inhou):
                    if hurtx == obj_hurt[list]._x and hurty == obj_hurt[list]._y:
                        listindex = list
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
                    obj_hurt[listindex].setx(0)
                    obj_example.decrease()

                    total = obj_board.printboard(2)
                    new_array.append(total)
            else:
                obj_town.hitpoint()
                if obj_town.hitpoints > 50 and obj_town.hitpoints < 100:
                    obj_town.shape = [[CH1, CH1, CH1], [
                        CH1, CH1, CH1], [CH1, CH1, CH1], [CH1, CH1, CH1]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)

                if obj_town.hitpoints > 20 and obj_town.hitpoints < 50:
                    obj_town.shape = [[CH2, CH2, CH2], [
                        CH2, CH2, CH2], [CH2, CH2, CH2], [CH2, CH2, CH2]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)

                if obj_town.hitpoints > 0 and obj_town.hitpoints < 20:
                    obj_town.shape = [[CH3, CH3, CH3], [
                        CH3, CH3, CH3], [CH3, CH3, CH3], [CH3, CH3, CH3]]
                    obj_town.show(
                        obj_board.grid, obj_town.shape, 20, 40)
                    os.system('clear')
                    obj_board.print_board(2)

                    total = obj_board.printboard(2)
                    new_array.append(total)

                elif obj_town.hitpoints <= 0:
                    # obj_hurt[listindex].shape=[[HURT1]]
                    # obj_hurt[listindex].show(obj_board.grid,obj_hurt[listindex].shape,hurtx,hurty)
                    for x in range(20, 24):
                        for y in range(40, 43):
                            obj_board.grid[x][y] = BACK
                    os.system('clear')
                    obj_board.print_board(2)
                    obj_example.decrease()

                    total = obj_board.printboard(2)
                    new_array.append(total)

obj_dum=dum()
val1 = random.randint(0, HEIGHT-5)
val2 = random.randint(0, WIDTH-10)
while obj_board.grid[val1][val2] != BACK:
    val1 = random.randint(0, HEIGHT-5)
    val2 = random.randint(0, WIDTH-10)
    # obj_king.king_clear(obj_board.grid)
valu1 = random.randint(0, HEIGHT-5)
valu2 = random.randint(0, WIDTH-10)
while obj_board.grid[val1][val2] != BACK:
    valu1 = random.randint(0, HEIGHT-5)
    valu2 = random.randint(0, WIDTH-10)

value1 = random.randint(0, HEIGHT-5)
value2 = random.randint(0, WIDTH-10)
while obj_board.grid[val1][val2] != BACK:
    value1 = random.randint(0, HEIGHT-5)
    value2 = random.randint(0, WIDTH-10)
    # obj_king.king_clear(obj_board.grid)

obj_troop2 = troop(value1, value2)
# obj_king.king_clear(obj_board.grid)

obj_troop = troop(val1, val2)
obj_troop1 = troop(valu1, valu2)

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
obj_archer=[]
xarcher1 = random.randint(0, HEIGHT-5)
yarcher1 = random.randint(0, WIDTH-10)
while obj_board.grid[xarcher1][yarcher1] != BACK:
    xarcher1 = random.randint(0, HEIGHT-5)
    yarcher1 = random.randint(0, WIDTH-10)

obj_archer1=[]
xarcher2 = random.randint(0, HEIGHT-5)
yarcher2 = random.randint(0, WIDTH-10)
while obj_board.grid[xarcher2][yarcher2] != BACK:
    xarcher2 = random.randint(0, HEIGHT-5)
    yarcher2 = random.randint(0, WIDTH-10)
obj_archer2=[]
# global sam
def sathvi(listindex, hurtx, hurty,damage):
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
def wallhitpoints(listindex, hurtx, hurty,damage):
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


# obj_archer=[]
obj_very=very()
obj_dum1=dum()
obj_dum2=dum()
obj_dum3=dum()
obj_dumx=dum()

sathtime=-1
def spwan():
    global sathtime
    # dum=troop1
    # global troop1
    
    # global obj_troop
    # global obj_troop1
    # global obj_troop2
    # print("ss")

    char = input_to(obj_get, 0.08)
    if char == 'I':
        #    sam=1
        # val1 = random.randint(0, HEIGHT-5)
        # val2 = random.randint(0, WIDTH-10)
        # while obj_board.grid[val1][val2] != BACK:
        #     val1 = random.randint(0, HEIGHT-5)
        #     val2 = random.randint(0, WIDTH-10)
        # # obj_king.king_clear(obj_board.grid)

        # obj_troop = troop(val1, val2)
        obj_troop.troop_show(obj_board.grid, val1, val2)
        obj_troop.setvalue(1)
        # tropid=tropid+1

        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    elif char == 'M':
        # val1 = random.randint(0, HEIGHT-5)
        # val2 = random.randint(0, WIDTH-10)
        # while obj_board.grid[val1][val2] != BACK:
        #     val1 = random.randint(0, HEIGHT-5)
        #     val2 = random.randint(0, WIDTH-10)
        # # obj_king.king_clear(obj_board.grid)

        # obj_troop1 = troop(val1, val2)
        obj_troop1.troop_show(obj_board.grid, valu1, valu2)
        # obj_board.print_board(2)
        total = obj_board.printboard(2)
        new_array.append(total)
        # tropid=tropid+1

        os.system('clear')
        obj_board.print_board(2)

    elif char == 'N':
        # val1 = random.randint(0, HEIGHT-5)
        # val2 = random.randint(0, WIDTH-10)
        # while obj_board.grid[val1][val2] != BACK:
        #     val1 = random.randint(0, HEIGHT-5)
        #     val2 = random.randint(0, WIDTH-10)
        # # obj_king.king_clear(obj_board.grid)

        # obj_troop2 = troop(val1, val2)
        obj_troop2.troop_show(obj_board.grid, value1, value2)
        # tropid=tropid+1

        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
    
    if char == 'L':
        #print("L")
        # obj_archer.append(Archer(vl1,vl2))
        #obj_very.setx(1)
        # vl1 = random.randint(0, HEIGHT-5)
        # vl2 = random.randint(0, WIDTH-10)
        # while obj_board.grid[vl1][vl2] != BACK:
        #   vl1 = random.randint(0, HEIGHT-5)
        #   vl2 = random.randint(0, WIDTH-10)
        obj_archer.append(Archer(vl1,vl2))
        obj_archer[obj_dum.getx()].Archer_show(obj_board.grid, vl1, vl2)
        obj_archer[obj_dum.getx()].setvalue(1)
        obj_dum.setx(1)
        # print("s")
        # obj_archer.setvalue(1)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)

    if char == 'G':
        #print("L")
        # obj_archer.append(Archer(vl1,vl2))
        #obj_very.setx(1)
        
        obj_archer1.append(Archer(xarcher1,yarcher1))
        obj_archer1[obj_dum1.getx()].Archer_show(obj_board.grid, xarcher1,yarcher1)
        obj_archer1[obj_dum1.getx()].setvalue(1)
        obj_dum1.setx(1)
        # print("s")
        # obj_archer.setvalue(1)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
    
    if char == 'H':
        #print("L")
        # obj_archer.append(Archer(vl1,vl2))
        #obj_very.setx(1)
        
        obj_archer2.append(Archer(xarcher2,yarcher2))
        obj_archer2[obj_dum2.getx()].Archer_show(obj_board.grid, xarcher2,yarcher2)
        obj_archer2[obj_dum2.getx()].setvalue(1)
        obj_dum2.setx(1)
        # print("s")
        # obj_archer.setvalue(1)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
    if char == 'X':
        obj_dumx.setx(1)
        sathtime=time.time()

   

        #print("L")
        # obj_archer.append(Archer(vl1,vl2))
        #obj_very.setx(1)




    

    

    

# x = obj_troop.getx_p()
# y = obj_troop.gety_p()
#         # print(y)
# finalx = x
# finaly = y
# min = 10000
# for list in range(0, inhou):
#     spr1 = obj_hurt[list].getx()
#     spr2 = obj_hurt[list].gety()
#     dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
#     if min > dist:
#         min = dist

#         finalx = spr1
#         finaly = spr2
#         # print(finalx)
# obj_troop.finalx(finalx)
# obj_troop.finaly(finaly)
def cannonhealth1(list,x1,y1,damage):
    #print("c")
    obj_cannon[list].hitss(damage)
    print(obj_cannon[list].hitpoints)
    if obj_cannon[list].hitpoints > 50 and obj_cannon[list].hitpoints < 100:
        #print("in")
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
        obj_cannon[list]._live=0
        os.system('clear')
        # obj_cannon[list]._live=0
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
        obj_example.decrease()





def townhitpoints(x1,y1,damage):
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


archerht=time.time()

def create():
    obj_hurt.clear()
    inhou = 0
    # inhou1 = 10
    while inhou < 15:
       val1 = random.randint(0, HEIGHT-5)
       val2 = random.randint(0, WIDTH-10)
    # print(val1)
    # print(val2)
       i = 1
    # print("enter")
       for p in range(val1, val1+4):
            for s in range(val2, val2+3):
                if obj_board.grid[p][s] != BACK:
                  i = 0

       if(i == 1):
        obj_hurt.append(Magnet(val1, val2, 90))
        # print(obj_hurt[inhou].hitpoints)
        obj_hurt[inhou].show(obj_board.grid, obj_hurt[inhou].shape,
                             obj_hurt[inhou].getx(), obj_hurt[inhou].gety())
        inhou = inhou+1

# archerht=-1
def archer_move1(dd):
    # global archerpt
    archerpt=time.time()
    global archerht
    # print("h")
    x= obj_archer[dd].getx_p()
    y = obj_archer[dd].gety_p()
    # print(y)
    finalx = x
    finaly = y
    min = 10000
    sos=0
    for list in range(0, inhou):
        if(obj_hurt[list]._live == 1):
            sos=1
            spr1 = obj_hurt[list].getx()
            spr2 = obj_hurt[list].gety()
            dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
            if min > dist:
                min = dist

                finalx = spr1
                finaly = spr2

    for list in range(0, canno):
        if(obj_cannon[list]._live == 1):
            sos=1
            spr1 = obj_cannon[list].getx()
            spr2 = obj_cannon[list].gety()
            dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
            if min > dist:
                min = dist

                finalx = spr1
                finaly = spr2

    if obj_town._live==1: 
      sos=1      
      dist = ((((x - val1town)**2) + ((y-val2town)**2))**0.5)
      if min > dist:
        min = dist

        finalx = val1town
        finaly = val2town

        # else :
            # print("in")

    # print(finalx)
    obj_archer[dd].finalx(finalx)
    obj_archer[dd].finaly(finaly)
    # print(finalx)
    # print(finaly)
    movex = 0
    movey = 0
    # r=obj_troop.setreturn()
    # print(r)
    if(obj_archer[dd].setreturn() == 1 and sos==1):
        # print("s")
        x = obj_archer[dd].getx_p()
        y = obj_archer[dd].gety_p()
        fy = obj_archer[dd].getfy()
        fx = obj_archer[dd].getfx()
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

        for p in range(-1, 2):
            for s in range(-1, 2):
                if x+p>0 and x+p<HEIGHT and y+p>0 and y+p<WIDTH and obj_board.grid[x+p][y+s] == HURT :
                    # cos=1
                    move1x = x+p
                    move1y = y+s
                    for list in range(0, inhou):
                        # print("s")
                        if move1x == obj_hurt[list]._x and move1y == obj_hurt[list]._y:
                            obj_board.grid[move1x][move1y] = BACK
                            obj_hurt[list]._live = 0
                            cos = 1
                
                if x+p>0 and x+p<HEIGHT and y+p>0 and y+p<WIDTH and obj_board.grid[x+p][y+s]==CH:
                    cos=1
                    move1x=x+p
                    move1y=y+s

                if x+p>0 and x+p<HEIGHT and y+p>0 and y+p<WIDTH and obj_board.grid[x+p][y+s] == CAN :
                    # cos=1
                    move1x = x+p
                    move1y = y+s
                    for list in range(0, canno):
                        # print("s")
                        if move1x == obj_cannon[list].getx() and move1y == obj_cannon[list].gety():
                            obj_board.grid[move1x][move1y] = BACK
                            obj_cannon[list]._live = 0
                            cos = 1
        pru=0     
        for o in range(x-7,x+8):
            # print(o)
            # print(obj_queen.getx_p())
            for p in range(y-7,y+8):
                # print(o)
                # print(obj_queen.getx_p())
                # archerpt=time.time()
                for list in range(0,inhou):
                    archerpt=time.time()
                    if o==obj_hurt[list]._x and p==obj_hurt[list]._y  and obj_hurt[list]._live==1:
                       obj_archer[dd].co=1
                    #   archerht=time.time()
                       while obj_hurt[list].hitpoints >=0 :
                        # archerpt=time.time()

                        if time.time()-archerht>0.5:
                        # global stime
                        # stime=time.time()
                          #SS=SS+1
                          archerht=time.time()
                        # if(Attime-stime>0.0005):
                        #   if SS%10==0:
                          sathvi(list,o,p,obj_archer[dd].damage)

                       obj_archer[dd].co=0
                        #   Attime=stime
                      
                
                    #   sathvi(list,o,p,obj_archer[dd].damage)
                # archerpt=time.time()
                for list in range(0,canno):
                    archerpt=time.time()
                    if o==obj_cannon[list].getx() and p==obj_cannon[list].gety() and obj_cannon[list]._live==1:
                        obj_archer[dd].co=1
                        while obj_cannon[list].hitpoints >=0 :
                        # archerpt=time.time()
                        # global stime
                        # stime=time.time()
                           if time.time()-archerht>0.5:
                        #    archerht=time.time()
                        #    SS=SS+1
                        # if(Attime-stime>0.0005):
                        #    if SS%10==0:
                              cannonhealth1(list,o,p,obj_archer[dd].damage)
                              archerht=time.time()
                        #   Attime=stime
                        obj_archer[dd].co=0
                        archerht=time.time()
                # archerpt=time.time()
                if o==val1town and p==val2town  :
                    obj_archer[dd].co=1
                    while obj_town.hitpoints >=0 :
                        
                        if time.time()-archerht>0.5:
                           townhitpoints(val1town,val2town,obj_archer[dd].damage)
                           archerht=time.time()
                    obj_archer[dd].co=0
                    
                    # archerht=time.time()

        
        
        # print(cos)
        if cos == 0 and obj_archer[dd].co==0 :
            

            if x-1>0 and obj_board.grid[x-1][y]==BACK or obj_board.grid[x-1][y]==WALL:
                dist1 = ((((x-1 - fx)**2) + ((y-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y

            if x+1<HEIGHT and obj_board.grid[x+1][y]==BACK or obj_board.grid[x+1][y]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y

            if  y+1<WIDTH and obj_board.grid[x][y+1]==BACK or obj_board.grid[x][y+1]==WALL:
                dist1 = ((((x- fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x
                    movey = y+1

            if y-1>0 and obj_board.grid[x][y-1]==BACK or obj_board.grid[x][y-1]==WALL:
                dist1 = ((((x - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x
                    movey = y-1

            if x-1>0 and y-1>0 and obj_board.grid[x-1][y-1]==BACK or obj_board.grid[x-1][y-1]==WALL:
                dist1 = ((((x-1 - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y-1

            if x+1<HEIGHT and y+1<WIDTH and obj_board.grid[x+1][y+1]==BACK or obj_board.grid[x+1][y+1]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y+1

            if  y+1<WIDTH and x-1>0 and obj_board.grid[x-1][y+1]==BACK or obj_board.grid[x-1][y+1]==WALL:
                dist1 = ((((x-1- fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y+1

            if y-1>0 and x+1<HEIGHT and obj_board.grid[x+1][y-1]==BACK or obj_board.grid[x+1][y-1]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y-1

            for list in range(0,walls):
                if movex==obj_walls[list]._x and movey==obj_walls[list]._y and obj_walls[list]._live==1:
                    while obj_walls[list].hitpoints >=0:
                       
                        #obj_walls[list].hitss(obj_archer[dd].damage)
                        wallhitpoints(list,movex,movey,obj_archer[dd].damage)
                    obj_board.grid[movex][movey]=BACK
                    obj_walls[list]._live=0
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
            obj_archer[dd].Archer_clear(obj_board.grid)

            obj_archer[dd].Archer_move(obj_board.grid, movex, movey)
            obj_archer[dd].sety_p(movey)
            obj_archer[dd].setx_p(movex)
            obj_archer[dd].Archer_show(obj_board.grid, movex, movey)
            os.system('clear')
            obj_board.print_board(2)
        # else:
        #     for list in range(0, inhou):
        #         # print("s")
        #         if move1x == obj_hurt[list]._x and move1y == obj_hurt[list]._y:
        #             # global Attime
        #             # Attime=time.time()

        #             # obj_board.grid[move1x][move1y] = BACK
        #             # print("ss")
        #             SS=0
        #             # archerpt=time.time()
        #             while obj_hurt[list].hitpoints >=0 :
        #                 archerpt=time.time()

        #                 if archerpt-archerht>2:
        #                 # global stime
        #                 # stime=time.time()
        #                   SS=SS+1
        #                   archerht=time.time()
        #                 # if(Attime-stime>0.0005):
        #                   if SS%10==0:
        #                      sathvi(list,move1x,move1y,obj_archer[dd].damage)
        #                 #   Attime=stime
        #                 # else :
        #                 #     # time.sleep(0.5)

        #                 #     sathvi(list,move1x,move1y)
        #                 #   Attime=stime
        #                 # archerht=time.time()


                        
        #             # obj_hurt[list]._live = 0
        #             cos = 0

        #     for list in range(0, canno):
        #         # print("s")
        #         if move1x == obj_cannon[list]._x and move1y == obj_cannon[list]._y:
        #             # global Attime
        #             # Attime=time.time()

        #             # obj_board.grid[move1x][move1y] = BACK
        #             # print("ss")
        #             SS=0
        #             while obj_cannon[list].hitpoints >=0 :
        #                 archerpt=time.time()
        #                 # global stime
        #                 # stime=time.time()
        #                 if archerpt-archerht>2:
        #                    archerht=time.time()
        #                    SS=SS+1
        #                 # if(Attime-stime>0.0005):
        #                    if SS%10==0:
        #                       cannonhealth1(list,move1x,move1y,obj_archer[dd].damage)
        #                 #   Attime=stime
        #                 # else :
        #                 #     # time.sleep(0.5)

        #                 #     sathvi(list,move1x,move1y)
        #                 #   Attime=stime


                        
        #             # obj_hurt[list]._live = 0
        #             cos = 0

        #     if move1x == val1town and move1y == val2town:
        #             # global Attime
        #             # Attime=time.time()

        #             # obj_board.grid[move1x][move1y] = BACK
        #             # print("ss")
        #         SS=0
        #         while obj_town.hitpoints >=0 :
        #                 # global stime
        #                 # stime=time.time()
        #                 # SS=SS+1
        #                 # if(Attime-stime>0.0005):
        #             archerpt=time.time()
        #             if archerpt-archerht>2:
        #                 archerht=time.time()
        #                 if SS%10==0:
        #                     townhitpoints(val1town,val2town,obj_archer[dd].damage)
        #                 #   Attime=stime
        #                 # else :
        #                 #     # time.sleep(0.5)

        #                 #     sathvi(list,move1x,move1y)
        #                 #   Attime=stime


                        
        #             # obj_hurt[list]._live = 0
        #         cos = 0


def archer_move2(dd):
    # print("h")
    x= obj_archer1[dd].getx_p()
    y = obj_archer1[dd].gety_p()
    # print(y)
    finalx = x
    finaly = y
    min = 10000
    sos=0
    for list in range(0, inhou):
        if(obj_hurt[list]._live == 1):
            sos=1
            spr1 = obj_hurt[list].getx()
            spr2 = obj_hurt[list].gety()
            dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
            if min > dist:
                min = dist

                finalx = spr1
                finaly = spr2

    for list in range(0, canno):
        if(obj_cannon[list]._live == 1):
            sos=1
            spr1 = obj_cannon[list].getx()
            spr2 = obj_cannon[list].gety()
            dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
            if min > dist:
                min = dist

                finalx = spr1
                finaly = spr2

    if obj_town._live==1: 
      sos=1      
      dist = ((((x - val1town)**2) + ((y-val2town)**2))**0.5)
      if min > dist:
        min = dist

        finalx = val1town
        finaly = val2town

        # else :
            # print("in")

    # print(finalx)
    obj_archer1[dd].finalx(finalx)
    obj_archer1[dd].finaly(finaly)
    # print(finalx)
    # print(finaly)
    movex = 0
    movey = 0
    # r=obj_troop.setreturn()
    # print(r)
    if(obj_archer1[dd].setreturn() == 1 and sos==1):
        # print("s")
        x = obj_archer1[dd].getx_p()
        y = obj_archer1[dd].gety_p()
        fy = obj_archer1[dd].getfy()
        fx = obj_archer1[dd].getfx()
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

        for p in range(-1, 2):
            for s in range(-1, 2):
                if x+p>0 and x+p<HEIGHT and y+p>0 and y+p<WIDTH and obj_board.grid[x+p][y+s] == HURT :
                    # cos=1
                    move1x = x+p
                    move1y = y+s
                    for list in range(0, inhou):
                        # print("s")
                        if move1x == obj_hurt[list]._x and move1y == obj_hurt[list]._y:
                            obj_board.grid[move1x][move1y] = BACK
                            obj_hurt[list]._live = 0
                            cos = 1
                
                if x+p>0 and x+p<HEIGHT and y+p>0 and y+p<WIDTH and obj_board.grid[x+p][y+s]==CH:
                    cos=1
                    move1x=x+p
                    move1y=y+s

                if x+p>0 and x+p<HEIGHT and y+p>0 and y+p<WIDTH and obj_board.grid[x+p][y+s] == CAN :
                    # cos=1
                    move1x = x+p
                    move1y = y+s
                    for list in range(0, canno):
                        # print("s")
                        if move1x == obj_cannon[list].getx() and move1y == obj_cannon[list].gety():
                            obj_board.grid[move1x][move1y] = BACK
                            obj_cannon[list]._live = 0
                            cos = 1
                
        for o in range(x-7,x+8):
            # print(o)
            # print(obj_queen.getx_p())
            for p in range(y-7,y+8):
                # print(o)
                # print(obj_queen.getx_p())
                for list in range(0,inhou):
                    if o==obj_hurt[list]._x and p==obj_hurt[list]._y:
                        
                           sathvi(list,o,p,obj_archer1[dd].damage)
                        
                for list in range(0,canno):
                    if o==obj_cannon[list].getx() and p==obj_cannon[list].gety():
                        
                           cannonhealth1(list,o,p,obj_archer1[dd].damage)
                
                if o==val1town and p==val2town:
                    
                        townhitpoints(val1town,val2town,obj_archer1[dd].damage)

        
        
        # print(cos)
        if cos == 0 :
            
            if x-1>0 and obj_board.grid[x-1][y]==BACK or obj_board.grid[x-1][y]==WALL:
                dist1 = ((((x-1 - fx)**2) + ((y-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y

            if x+1<HEIGHT and obj_board.grid[x+1][y]==BACK or obj_board.grid[x+1][y]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y

            if  y+1<WIDTH and obj_board.grid[x][y+1]==BACK or obj_board.grid[x][y+1]==WALL:
                dist1 = ((((x- fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x
                    movey = y+1

            if y-1>0 and obj_board.grid[x][y-1]==BACK or obj_board.grid[x][y-1]==WALL:
                dist1 = ((((x - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x
                    movey = y-1

            if x-1>0 and y-1>0 and obj_board.grid[x-1][y-1]==BACK or obj_board.grid[x-1][y-1]==WALL:
                dist1 = ((((x-1 - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y-1

            if x+1<HEIGHT and y+1<WIDTH and obj_board.grid[x+1][y+1]==BACK or obj_board.grid[x+1][y+1]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y+1

            if  y+1<WIDTH and x-1>0 and obj_board.grid[x-1][y+1]==BACK or obj_board.grid[x-1][y+1]==WALL:
                dist1 = ((((x-1- fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y+1

            if y-1>0 and x+1<HEIGHT and obj_board.grid[x+1][y-1]==BACK or obj_board.grid[x+1][y-1]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y-1

            for list in range(0,walls):
                if movex==obj_walls[list]._x and movey==obj_walls[list]._y and obj_walls[list]._live==1:
                    while obj_walls[list].hitpoints >=0:
                       
                        #obj_walls[list].hitss(obj_archer[dd].damage)
                        wallhitpoints(list,movex,movey,obj_archer1[dd].damage)
                    obj_board.grid[movex][movey]=BACK
                    obj_walls[list]._live=0
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
            obj_archer1[dd].Archer_clear(obj_board.grid)

            obj_archer1[dd].Archer_move(obj_board.grid, movex, movey)
            obj_archer1[dd].sety_p(movey)
            obj_archer1[dd].setx_p(movex)
            obj_archer1[dd].Archer_show(obj_board.grid, movex, movey)
            os.system('clear')
            obj_board.print_board(2)
        else:
            for list in range(0, inhou):
                # print("s")
                if move1x == obj_hurt[list]._x and move1y == obj_hurt[list]._y:
                    # global Attime
                    # Attime=time.time()

                    # obj_board.grid[move1x][move1y] = BACK
                    # print("ss")
                    SS=0
                    while obj_hurt[list].hitpoints >=0:
                        global stime
                        stime=time.time()
                        SS=SS+1
                        # if(Attime-stime>0.0005):
                        if SS%10==0:
                           sathvi(list,move1x,move1y,obj_archer1[dd].damage)
                        #   Attime=stime
                        # else :
                        #     # time.sleep(0.5)

                        #     sathvi(list,move1x,move1y)
                        #   Attime=stime


                        
                    # obj_hurt[list]._live = 0
                    cos = 0

            for list in range(0, canno):
                # print("s")
                if move1x == obj_cannon[list]._x and move1y == obj_cannon[list]._y:
                    # global Attime
                    # Attime=time.time()

                    # obj_board.grid[move1x][move1y] = BACK
                    # print("ss")
                    SS=0
                    while obj_cannon[list].hitpoints >=0:
                        # global stime
                        # stime=time.time()
                        SS=SS+1
                        # if(Attime-stime>0.0005):
                        if SS%10==0:
                           cannonhealth1(list,move1x,move1y,obj_archer1[dd].damage)
                        #   Attime=stime
                        # else :
                        #     # time.sleep(0.5)

                        #     sathvi(list,move1x,move1y)
                        #   Attime=stime


                        
                    # obj_hurt[list]._live = 0
                    cos = 0

            if move1x == val1town and move1y == val2town:
                    # global Attime
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
                        townhitpoints(val1town,val2town,obj_archer1[dd].damage)
                        #   Attime=stime
                        # else :
                        #     # time.sleep(0.5)

                        #     sathvi(list,move1x,move1y)
                        #   Attime=stime


                        
                    # obj_hurt[list]._live = 0
                cos = 0


def archer_move3(dd):
    # print("h")
    x= obj_archer2[dd].getx_p()
    y = obj_archer2[dd].gety_p()
    # print(y)
    finalx = x
    finaly = y
    min = 10000
    sos=0
    for list in range(0, inhou):
        if(obj_hurt[list]._live == 1):
            sos=1
            spr1 = obj_hurt[list].getx()
            spr2 = obj_hurt[list].gety()
            dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
            if min > dist:
                min = dist

                finalx = spr1
                finaly = spr2

    for list in range(0, canno):
        if(obj_cannon[list]._live == 1):
            sos=1
            spr1 = obj_cannon[list].getx()
            spr2 = obj_cannon[list].gety()
            dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
            if min > dist:
                min = dist

                finalx = spr1
                finaly = spr2

    if obj_town._live==1: 
      sos=1      
      dist = ((((x - val1town)**2) + ((y-val2town)**2))**0.5)
      if min > dist:
        min = dist

        finalx = val1town
        finaly = val2town

        # else :
            # print("in")

    # print(finalx)
    obj_archer2[dd].finalx(finalx)
    obj_archer2[dd].finaly(finaly)
    # print(finalx)
    # print(finaly)
    movex = 0
    movey = 0
    # r=obj_troop.setreturn()
    # print(r)
    if(obj_archer2[dd].setreturn() == 1 and sos==1):
        # print("s")
        x = obj_archer2[dd].getx_p()
        y = obj_archer2[dd].gety_p()
        fy = obj_archer2[dd].getfy()
        fx = obj_archer2[dd].getfx()
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

        for p in range(-1, 2):
            for s in range(-1, 2):
                if x+p>0 and x+p<HEIGHT and y+p>0 and y+p<WIDTH and obj_board.grid[x+p][y+s] == HURT :
                    # cos=1
                    move1x = x+p
                    move1y = y+s
                    for list in range(0, inhou):
                        # print("s")
                        if move1x == obj_hurt[list]._x and move1y == obj_hurt[list]._y:
                           obj_board.grid[move1x][move1y] = BACK
                           obj_hurt[list]._live = 0
                           cos = 1
                
                if x+p>0 and x+p<HEIGHT and y+p>0 and y+p<WIDTH and obj_board.grid[x+p][y+s]==CH:
                    cos=1
                    move1x=x+p
                    move1y=y+s

                if x+p>0 and x+p<HEIGHT and y+p>0 and y+p<WIDTH and obj_board.grid[x+p][y+s] == CAN :
                    # cos=1
                    move1x = x+p
                    move1y = y+s
                    for list in range(0, canno):
                        # print("s")
                        if move1x == obj_cannon[list].getx() and move1y == obj_cannon[list].gety():
                            obj_board.grid[move1x][move1y] = BACK
                            obj_cannon[list]._live = 0
                            cos = 1
                
        for o in range(x-7,x+8):
            # print(o)
            # print(obj_queen.getx_p())
            for p in range(y-7,y+8):
                # print(o)
                # print(obj_queen.getx_p())
                for list in range(0,inhou):
                    if o==obj_hurt[list]._x and p==obj_hurt[list]._y:
                       
                        sathvi(list,o,p,obj_archer2[dd].damage)
                for list in range(0,canno):
                    if o==obj_cannon[list].getx() and p==obj_cannon[list].gety():
                        
                        cannonhealth1(list,o,p,obj_archer2[dd].damage)
                
                if o==val1town and p==val2town:
                    
                    townhitpoints(val1town,val2town,obj_archer2[dd].damage)

        
        
        # print(cos)
        if cos == 0 :
            

            if x-1>0 and obj_board.grid[x-1][y]==BACK or obj_board.grid[x-1][y]==WALL:
                dist1 = ((((x-1 - fx)**2) + ((y-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y

            if x+1<HEIGHT and obj_board.grid[x+1][y]==BACK or obj_board.grid[x+1][y]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y

            if  y+1<WIDTH and obj_board.grid[x][y+1]==BACK or obj_board.grid[x][y+1]==WALL:
                dist1 = ((((x- fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x
                    movey = y+1

            if y-1>0 and obj_board.grid[x][y-1]==BACK or obj_board.grid[x][y-1]==WALL:
                dist1 = ((((x - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x
                    movey = y-1

            if x-1>0 and y-1>0 and obj_board.grid[x-1][y-1]==BACK or obj_board.grid[x-1][y-1]==WALL:
                dist1 = ((((x-1 - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y-1

            if x+1<HEIGHT and y+1<WIDTH and obj_board.grid[x+1][y+1]==BACK or obj_board.grid[x+1][y+1]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y+1

            if  y+1<WIDTH and x-1>0 and obj_board.grid[x-1][y+1]==BACK or obj_board.grid[x-1][y+1]==WALL:
                dist1 = ((((x-1- fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y+1

            if y-1>0 and x+1<HEIGHT and obj_board.grid[x+1][y-1]==BACK or obj_board.grid[x+1][y-1]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y-1

            for list in range(0,walls):
                if movex==obj_walls[list]._x and movey==obj_walls[list]._y and obj_walls[list]._live==1:
                    while obj_walls[list].hitpoints >=0:
                       
                        #obj_walls[list].hitss(obj_archer[dd].damage)
                        wallhitpoints(list,movex,movey,obj_archer2[dd].damage)
                    obj_board.grid[movex][movey]=BACK
                    obj_walls[list]._live=0
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
            obj_archer2[dd].Archer_clear(obj_board.grid)

            obj_archer2[dd].Archer_move(obj_board.grid, movex, movey)
            obj_archer2[dd].sety_p(movey)
            obj_archer2[dd].setx_p(movex)
            obj_archer2[dd].Archer_show(obj_board.grid, movex, movey)
            os.system('clear')
            obj_board.print_board(2)
        else:
            for list in range(0, inhou):
                # print("s")
                if move1x == obj_hurt[list]._x and move1y == obj_hurt[list]._y:
                    # global Attime
                    # Attime=time.time()

                    # obj_board.grid[move1x][move1y] = BACK
                    # print("ss")
                    SS=0
                    while obj_hurt[list].hitpoints >=0:
                        global stime
                        stime=time.time()
                        SS=SS+1
                        # if(Attime-stime>0.0005):
                        if SS%10==0:
                           sathvi(list,move1x,move1y,obj_archer2[dd].damage)
                        #   Attime=stime
                        # else :
                        #     # time.sleep(0.5)

                        #     sathvi(list,move1x,move1y)
                        #   Attime=stime


                        
                    # obj_hurt[list]._live = 0
                    cos = 0

            for list in range(0, canno):
                # print("s")
                if move1x == obj_cannon[list]._x and move1y == obj_cannon[list]._y:
                    # global Attime
                    # Attime=time.time()

                    # obj_board.grid[move1x][move1y] = BACK
                    # print("ss")
                    SS=0
                    while obj_cannon[list].hitpoints >=0:
                        # global stime
                        # stime=time.time()
                        SS=SS+1
                        # if(Attime-stime>0.0005):
                        if SS%10==0:
                           cannonhealth1(list,move1x,move1y,obj_archer2[dd].damage)
                        #   Attime=stime
                        # else :
                        #     # time.sleep(0.5)

                        #     sathvi(list,move1x,move1y)
                        #   Attime=stime


                        
                    # obj_hurt[list]._live = 0
                    cos = 0

            if move1x == val1town and move1y == val2town:
                    # global Attime
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
                        townhitpoints(val1town,val2town,obj_archer2[dd].damage)
                        #   Attime=stime
                        # else :
                        #     # time.sleep(0.5)

                        #     sathvi(list,move1x,move1y)
                        #   Attime=stime


                        
                    # obj_hurt[list]._live = 0
                cos = 0




def troopmove():
    # print("tr")
    global initaltime
    intialtime=time.time()
    x = obj_troop.getx_p()
    y = obj_troop.gety_p()
    # print(y)
    finalx = x
    finaly = y
    min = 10000
    sos=0
    for list in range(0, inhou):
        if(obj_hurt[list]._live == 1):
            sos=1
            spr1 = obj_hurt[list].getx()
            spr2 = obj_hurt[list].gety()
            dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
            if min > dist:
                min = dist

                finalx = spr1
                finaly = spr2
        # else :
            # print("in")

    # print(finalx)
    obj_troop.finalx(finalx)
    obj_troop.finaly(finaly)
    # print(finalx)
    # print(finaly)
    movex = 0
    movey = 0
    # r=obj_troop.setreturn()
    # print(r)
    if(obj_troop.setreturn() == 1 and sos==1):
        # print("s")
        x = obj_troop.getx_p()
        y = obj_troop.gety_p()
        fy = obj_troop.getfy()
        fx = obj_troop.getfx()
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

        for p in range(-1, 2):
            for s in range(-1, 2):
                if p==0 and s==0:
                    sath1=0
                else :
                   if x+p>0 and x+p<HEIGHT and y+p>0 and y+p<WIDTH and obj_board.grid[x+p][y+s] == HURT:
                      move1x = x+p
                      move1y = y+s
                      for list in range(0, inhou):
                        # print("s")
                        if move1x == obj_hurt[list]._x and move1y == obj_hurt[list]._y:
                            obj_board.grid[move1x][move1y] = BACK
                            obj_hurt[list]._live = 0
                            cos = 1

        # print(cos)
        if cos == 0:
            # print("s")
            if x-1>0 and obj_board.grid[x-1][y]==BACK or obj_board.grid[x-1][y]==WALL:
                dist1 = ((((x-1 - fx)**2) + ((y-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y

            if x+1<HEIGHT and obj_board.grid[x+1][y]==BACK or obj_board.grid[x+1][y]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y

            if  y+1<WIDTH and obj_board.grid[x][y+1]==BACK or obj_board.grid[x][y+1]==WALL:
                dist1 = ((((x- fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x
                    movey = y+1

            if y-1>0 and obj_board.grid[x][y-1]==BACK or obj_board.grid[x][y-1]==WALL:
                dist1 = ((((x - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x
                    movey = y-1

            if x-1>0 and y-1>0 and obj_board.grid[x-1][y-1]==BACK or obj_board.grid[x-1][y-1]==WALL:
                dist1 = ((((x-1 - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y-1

            if x+1<HEIGHT and y+1<WIDTH and obj_board.grid[x+1][y+1]==BACK or obj_board.grid[x+1][y+1]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y+1

            if  y+1<WIDTH and x-1>0 and obj_board.grid[x-1][y+1]==BACK or obj_board.grid[x-1][y+1]==WALL:
                dist1 = ((((x-1- fx)**2) + ((y+1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x-1
                    movey = y+1

            if y-1>0 and x+1<HEIGHT and obj_board.grid[x+1][y-1]==BACK or obj_board.grid[x+1][y-1]==WALL:
                dist1 = ((((x+1 - fx)**2) + ((y-1-fy)**2))**0.5)
                if(mindis > dist1):
                    mindis = dist1
                    movex = x+1
                    movey = y-1

                        
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
            #         dist1=((((p - finalx )**2) + ((s-finaly)**2) )**0.5)
            #         if( mindis >dist1):
            #             mindis=dist1
            #             movex=p
            #             movey=s

        # print(movex)
        # print(movey)
            obj_troop.troop_clear(obj_board.grid)

            obj_troop.troop_move(obj_board.grid, movex, movey)
            obj_troop.sety_p(movey)
            obj_troop.setx_p(movex)
            obj_troop.troop_show(obj_board.grid, movex, movey)
            os.system('clear')
            obj_board.print_board(2)
        else:
            for list in range(0, inhou):
                # print("s")
                if move1x == obj_hurt[list]._x and move1y == obj_hurt[list]._y:
                    # global Attime
                    # Attime=time.time()

                    # obj_board.grid[move1x][move1y] = BACK
                    # print("ss")
                    SS=0
                    while obj_hurt[list].hitpoints >=0:
                        global stime
                        stime=time.time()
                        SS=SS+1
                        # if(Attime-stime>0.0005):
                        if SS%10==0:
                           sathvi(list,move1x,move1y)
                        #   Attime=stime
                        # else :
                        #     # time.sleep(0.5)

                        #     sathvi(list,move1x,move1y)
                        #   Attime=stime


                        
                    # obj_hurt[list]._live = 0
                    cos = 0

                
# obj_archer=[]
# obj_very=very()
archers=0
def rupa():
    print("l")
    char = input_to(obj_get, 0.08)
    if char == 'L':
        archers=archers+1
        #print("L")
        
        obj_archer.Archer_show(obj_board.grid, vl1, vl2)
        # print("s")
        obj_archer.setvalue(1)
        os.system('clear')
        obj_board.print_board(2)

        total = obj_board.printboard(2)
        new_array.append(total)
        # print(tropid)


# def archer_move1():
#     print("h")
#     x= obj_archer.getx_p()
#     y = obj_archer.gety_p()
#     # print(y)
#     finalx = x
#     finaly = y
#     min = 10000
#     for list in range(0, inhou):
#         if(obj_hurt[list]._live == 1):
#             spr1 = obj_hurt[list].getx()
#             spr2 = obj_hurt[list].gety()
#             dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
#             if min > dist:
#                 min = dist

#                 finalx = spr1
#                 finaly = spr2
#         else :
#             print("in")

#     # print(finalx)
#     obj_archer.finalx(finalx)
#     obj_archer.finaly(finaly)
#     # print(finalx)
#     # print(finaly)
#     movex = 0
#     movey = 0
#     # r=obj_troop.setreturn()
#     # print(r)
#     if(obj_archer.setreturn() == 1):
#         # print("s")
#         x = obj_archer.getx_p()
#         y = obj_archer.gety_p()
#         fy = obj_archer.getfy()
#         fx = obj_archer.getfx()
#         # # print(y)
#         # finalx = x
#         # finaly = y
#         # min = 10000
#         # for list in range(0, inhou):
#         #     spr1 = obj_hurt[list].getx()
#         #     spr2 = obj_hurt[list].gety()
#         #     dist = ((((x - spr1)**2) + ((y-spr2)**2))**0.5)
#         #     if min > dist:
#         #         min = dist
#         #         # print(min)
#         #         finalx = spr1
#         #         finaly = spr2
#         # # print(finalx)
#         # print(finaly)
#         mindis = 10000
#         movex = 0
#         movey = 0
#         move1x = 0
#         move1y = 0
#         cos = 0

#         for p in range(-1, 2):
#             for s in range(-1, 2):
#                 if obj_board.grid[x+p][y+s] == HURT:
#                     move1x = x+p
#                     move1y = y+s
#                     for list in range(0, inhou):
#                         # print("s")
#                         if move1x == obj_hurt[list]._x and move1y == obj_hurt[list]._y:
#                             obj_board.grid[move1x][move1y] = BACK
#                             obj_hurt[list]._live = 0
#                             cos = 1

#         # print(cos)
#         if cos == 0:
#             # print("s")
#             for p in range(-1, 2):
#                 for s in range(-1, 2):
#                     if obj_board.grid[x+p][y+s] == BACK or obj_board.grid[x+p][y+s]==WALL:
#                         if p == 0 and s == 0:

#                            sath = 1
#                         else:
#                             dist1 = ((((x+p - fx)**2) + ((y+s-fy)**2))**0.5)
#                             if(mindis > dist1):
#                                mindis = dist1
#                                movex = x+p
#                                movey = y+s
#                     # dist1=((((p - finalx )**2) + ((s-finaly)**2) )**0.5)
#                     # if( mindis >dist1):
#                     #     mindis=dist1
#                     #     movex=p
#                     #     movey=s

#         # print(movex)
#         # print(movey)
#             obj_archer.Archer_clear(obj_board.grid)

#             obj_archer.Archer_move(obj_board.grid, movex, movey)
#             obj_archer.sety_p(movey)
#             obj_archer.setx_p(movex)
#             obj_archer.Archer_show(obj_board.grid, movex, movey)
#             os.system('clear')
#             obj_board.print_board(2)
#         else:
#             for list in range(0, inhou):
#                 # print("s")
#                 if move1x == obj_hurt[list]._x and move1y == obj_hurt[list]._y:
#                     # global Attime
#                     # Attime=time.time()

#                     # obj_board.grid[move1x][move1y] = BACK
#                     # print("ss")
#                     SS=0
#                     while obj_hurt[list].hitpoints >=0:
#                         global stime
#                         stime=time.time()
#                         SS=SS+1
#                         # if(Attime-stime>0.0005):
#                         if SS%10==0:
#                            sathvi(list,move1x,move1y)
#                         #   Attime=stime
#                         # else :
#                         #     # time.sleep(0.5)

#                         #     sathvi(list,move1x,move1y)
#                         #   Attime=stime


                        
#                     # obj_hurt[list]._live = 0
#                     cos = 0

