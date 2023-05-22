from src.headers import *
from src.person import Person

class king(Person) :
    def __init__(self,x_p,y_p):
        self.__body=np.array([[" ","O"," "],["{","|","}"],["/"," ","\\"]])
        self.__body
        self.__floor=Fore.WHITE + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL
        Person.__init__(self,x_p,y_p)

    def king_clear(self,grid):
        x=self.getx_p()
        y=self.gety_p()
        for i in range(x,x+3):
            for j in range(y, y+3):
                grid[i][j]=self.__floor




    def king_show(self,grid,x,y):
        # if mode == 0:
        # self.din_clear(grid)
        self.setx_p(x)
        self.sety_p(y)
        for i in range(x,x+3):
            for j in range(y, y+3):
                grid[i][j]=self.__body[i-x][j-y]

    def king_move(self,grid,x,y):
        self.king_clear(grid)
        self.setx_p(x)
        self.sety_p(y)
        for i in range(x,x+3):
            for j in range(y, y+3):
                grid[i][j]=self.__body[i-x][j-y]




class troop(Person):
    def __init__(self,x_p,y_p):
        # self.__body=np.array([[" ","O"," "],["{","|","}"],["/"," ","\\"]])
        # self.__body
        self.cc=CHECK
        self.__body=Fore.RED + Back.BLACK + Style.BRIGHT +"T"+ Style.RESET_ALL
        self.__floor=Fore.BLACK + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL
        self.value=0
        self.finax=0
        self.finay=0
        Person.__init__(self,x_p,y_p)
    def setvalue(self,x):
        self.value=x
    def finalx(self,x):
        self.finax=x
    def finaly(self,x):
        self.finay=x
    def getfy(self):
        return self.finay
    def getfx(self):
        return self.finax


    

    def setreturn(self):
        return self.value



    def troop_show(self,grid,x,y):
        # if mode == 0:
        # self.din_clear(grid)
        self.setx_p(x)
        self.sety_p(y)
        grid[x][y]=self.__body

    def troop_clear(self,grid):
        x=self.getx_p()
        y=self.gety_p()
        grid[x][y]=self.__floor

    def troop_move(self,grid,x,y):
        self.troop_clear(grid)
        self.setx_p(x)
        self.sety_p(y)
        grid[x][y]=self.__body


class Archer(Person):
    def __init__(self,x_p,y_p):
        # self.__body=np.array([[" ","O"," "],["{","|","}"],["/"," ","\\"]])
        # self.__body
        self.cc=CHECK
        self.__body=Fore.GREEN + Back.BLACK + Style.BRIGHT +"A"+ Style.RESET_ALL
        self.__floor=Fore.BLACK + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL
        self.value=0
        self.finax=0
        self.finay=0
        self.damage=8
        self.health=50
        Person.__init__(self,x_p,y_p)
    def setvalue(self,x):
        self.value=x
    def finalx(self,x):
        self.finax=x
    def finaly(self,x):
        self.finay=x
    def getfy(self):
        return self.finay
    def getfx(self):
        return self.finax


    

    def setreturn(self):
        return self.value



    def Archer_show(self,grid,x,y):
        # if mode == 0:
        # self.din_clear(grid)
        self.setx_p(x)
        self.sety_p(y)
        grid[x][y]=self.__body

    def Archer_clear(self,grid):
        x=self.getx_p()
        y=self.gety_p()
        grid[x][y]=self.__floor

    def Archer_move(self,grid,x,y):
        self.Archer_clear(grid)
        self.setx_p(x)
        self.sety_p(y)
        grid[x][y]=self.__body



class Ballon(Person):
    def __init__(self,x_p,y_p):
        # self.__body=np.array([[" ","O"," "],["{","|","}"],["/"," ","\\"]])
        # self.__body
        self.cc=CHECK
        self.__body=Fore.GREEN + Back.BLACK + Style.BRIGHT +"B"+ Style.RESET_ALL
        self.__floor=Fore.BLACK + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL
        self.value=0
        self.finax=0
        self.finay=0
        self.damage=30
        self.health=100
        self.lasx=0
        self.lasy=0
        Person.__init__(self,x_p,y_p)

    

    def lastx(self,x):
        self.lasx=x
    def lasty(self,y):
        self.lasy=y
        
        
       
    

    # def sam(self,x):
         
    def lassx(self):
        return self.lasx

    def lassy(self):
        return self.lasy
    def setvalue(self,x):
        self.value=x
    def finalx(self,x):
        self.finax=x
    def finaly(self,x):
        self.finay=x
    def getfy(self):
        return self.finay
    def getfx(self):
        return self.finax


    

    def setreturn(self):
        return self.value



    def Ballon_show(self,grid,x,y):
        # if mode == 0:
        # self.din_clear(grid)
        self.setx_p(x)
        self.sety_p(y)
        grid[x][y]=self.__body

    def Ballon_clear(self,grid):
        x=self.getx_p()
        y=self.gety_p()
        grid[x][y]=self.__floor

    def Ballon_move(self,grid,x,y):
        self.Ballon_clear(grid)
        self.setx_p(x)
        self.sety_p(y)
        grid[x][y]=self.__body


    



