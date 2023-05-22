from src.headers import *

class Person:
    def __init__(self,x_p,y_p):
        self._x=x_p
        self._y=y_p
        self._live=1
        self.damage=15
        self.speed=1
        self.live=1
        self.health=100
        self.start=0
        self.sss=BACK
        self.co=0
    def getx_p(self):
        return self._x

    def setx_p(self,x):
        self._x= x

    def gety_p(self):
        return self._y

    def getdamage(self):
        return self.damage

    def getspeed(self):
        return self.speed
    
    
    def changehealth(self,damage):
        self.health = self.health-damage

    def sety_p(self,y):
       self._y= y

    

    def shells1(self,damage,speed):
        self.damage=damage
        self.speed=speed

    def shells(self):
        self.health=self.health+self.health/2
