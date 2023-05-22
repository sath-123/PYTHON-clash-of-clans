from src.headers import *

class Background:

    #constructor function
    def __init__(self):
        self.__ceil=Fore.YELLOW + Back.BLACK + Style.BRIGHT +"-" +Style.RESET_ALL 
        self.__ceil1=Fore.YELLOW+ Back.BLACK + Style.BRIGHT +"|" +Style.RESET_ALL       #Private variables to ensure security
        self.__floor=Fore.WHITE + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL
        # self.__middle=Fore.BLACK + Back.LIGHTYELLOW_EX + Style.BRIGHT +"="+Style.RESET_ALL

    #function to create the floor
    def display_floor(self,boundary):
        for i in range(HEIGHT-1):
            for j in range(WIDTH-1):

                boundary[i][j]= self.__floor
            # boundary[HEIGHT-2][i]=self.__middle
    
    def create_house(self,bou):
        # print("hh")
        for i in range(10,14):
            # print("jjj")
            for j in range(20,23):
                bou[i][j]='H'
                # print("enter")
    #function to create the ceil
    def display_ceil(self,boundary):
        for i in range(WIDTH-1):
            boundary[0][i]=self.__ceil

        for i in range(WIDTH-1):
            boundary[HEIGHT-2][i]=self.__ceil

        for i in range(HEIGHT-1):
            boundary[i][0]=self.__ceil1
        for i in range(HEIGHT-1):
            boundary[i][WIDTH-1]=self.__ceil1
            # boundary[1][i]=self.__middle

