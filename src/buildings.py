from src.headers import *

class buildings:
    def __init__(self,x,y,hitpoint):
        self.hitpoints=hitpoint
        self._x = x
        self._y = y
        self._live=1
       
    def setx(self, x):
        self._x=x
    def life(self,x):
        self._live=x
        
    def getlife(self):
        return self._live
    def sety(self,y):
        self._y=y
    def getx(self):
        return self._x
    def gety(self):
        return self._y
    def hitss(self,damage):
        self.hitpoints=self.hitpoints-damage
    def hitpoint(self):
        self.hitpoints=self.hitpoints-15

    def changecolor(self):
        self.shape=[[HURT1]]

    


    def show(self,grid,shape,x,y): 
        # print(x)                 
        #POLYMORPHISM USED TO SHOW/DISPLAY ALL OBJECTS
        for i in range(x,x+len(shape)):
            for j in range(y,y+len(shape[0])):
                grid[i][j]=shape[i-x][j-y]

    def attack(self,grid,x,y):
        if Direction==1:
            print("")



class Magnet(buildings):
    def __init__(self, x,y,hitpoint):
        self.shape=[[HURT]]
        self._live=0
        buildings.__init__(self,x,y,hitpoint)


class Townhall(buildings):
    def __init__(self, x,y,hitpoint):
        self.shape=[[CH,CH,CH],[CH,CH,CH],[CH,CH,CH],[CH,CH,CH]]
        buildings.__init__(self,x,y,hitpoint)

class cannon(buildings):
    def __init__(self,x,y,damage):
        self.shape=[[CAN,CAN,CAN],[CAN,CAN,CAN],[CAN,CAN,CAN]]
        buildings.__init__(self,x,y,damage)
        self._damage=20

class Walls(buildings):
    def __init__(self,x,y,damage):
        self.shape=[[WALL]]
        buildings.__init__(self,x,y,damage)
        self._damage=damage
    
class Wizard(buildings):
    def __init__(self,x,y,damage):
        self.shape=[[WIZ,WIZ,WIZ],[WIZ,WIZ,WIZ],[WIZ,WIZ,WIZ]]
        buildings.__init__(self,x,y,damage)
        self._damage=20
    
    

    





    
        