from src.headers import *
# from src.all import *
# from src.headers import *

# importing classes
from src.board import Boardofgame
from src.buildings import *
from src.back import Background
from src.king import *
from src.input import *
from src.examples import *
from src.queen import *
from src.all import *
def sathvika1(listindex, hurtx, hurty):
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


