
from src.headers import *
class example:
    def __init__(self,hitpoint):
        self.hitpoints=hitpoint
        
        
       
    def setx(self, x):
        self.hitpoints=x

    # def sam(self,x):
         
   
    def getx(self):
        return self.hitpoints
    def decrease(self):
        self.hitpoints=self.hitpoints-1
    

class verify:
    def __init__(self):
        self.ver=-1
        
        
       
    def setx(self, x):
        self.ver=x

    # def sam(self,x):
         
   
    def getx(self):
        return self.ver

class very:
    def __init__(self):
        self.very=-1
        
        
       
    def setx(self, x):
        self.very=x+self.very

    # def sam(self,x):
         
   
    def getx(self):
        return self.very

class dum:
    def __init__(self):
        self.very=0
        self.body=Fore.WHITE + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL

        self.lasx=0
        self.lasy=0

    def lastx(self,x):
        self.lasx=x
    def lasty(self,y):
        self.lasy=y
        
        
       
    def setx(self, x):
        self.very=x+self.very

    # def sam(self,x):
         
    def lassx(self):
        return self.lasx

    def lassy(self):
        return self.lasy
    def getx(self):
        return self.very

    
