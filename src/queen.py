from src.headers import *
from src.person import Person

class queen(Person) :
    def __init__(self,x_p,y_p):
        self.nan=QUEEN
        
        self.__floor=Fore.WHITE + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL
        Person.__init__(self,x_p,y_p)

    def queen_clear(self,grid):
        x=self.getx_p()
        y=self.gety_p()
        
        grid[x][y]=self.__floor




    def queen_show(self,grid,x,y):
        # if mode == 0:
        # self.din_clear(grid)
        self.setx_p(x)
        self.sety_p(y)
        grid[x][y]=self.nan

    def queen_move(self,grid,x,y):
        self.queen_clear(grid)
        self.setx_p(x)
        self.sety_p(y)
       
        grid[x][y]=self.nan




