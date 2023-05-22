from colorama import Fore, Back, Style
import numpy as np
import random
import os
import time
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

HEIGHT=55
WIDTH=160
SCREEN=150
head=-1
Direction=-1
hurtx=0
hurty=0
listindex=-1
obj_hurt=[]
new_array=[]
# sathvika=0
# global gameover
game=1

CHECK= Back.BLACK + Style.BRIGHT +"T"+ Style.RESET_ALL
CH= Fore.WHITE+Back.BLACK + Style.BRIGHT +"T"+ Style.RESET_ALL
CH1= Fore.YELLOW+Back.BLACK + Style.BRIGHT +"T"+ Style.RESET_ALL
CH2= Fore.GREEN+Back.BLACK + Style.BRIGHT +"T"+ Style.RESET_ALL
CH3= Fore.RED+Back.BLACK + Style.BRIGHT +"T"+ Style.RESET_ALL
HURT=Fore.LIGHTMAGENTA_EX+"x"+Style.RESET_ALL
HURT1=Fore.GREEN+"x"+Style.RESET_ALL
HURT2=Fore.RED+"x"+Style.RESET_ALL
HURT3=Fore.YELLOW+"x"+Style.RESET_ALL
BACK=Fore.WHITE + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL
QUEEN=Fore.GREEN+Back.BLACK+Style.BRIGHT+"Q"+Style.RESET_ALL
CAN=Fore.RED+Back.BLACK+"C"+Style.RESET_ALL
WALL=Fore.YELLOW+Back.BLACK+"W"+Style.RESET_ALL
WALL1=Fore.RED+Back.BLACK+"W"+Style.RESET_ALL
WALL2=Fore.GREEN+Back.BLACK+"W"+Style.RESET_ALL
WALL3=Fore.WHITE+Back.BLACK+"W"+Style.RESET_ALL
WIZ=Fore.WHITE+Back.BLACK+"O"+Style.RESET_ALL
QUE1=Fore.RED+Back.BLACK+Style.BRIGHT+"Q"+Style.RESET_ALL
QUE2=Fore.YELLOW+Back.BLACK+Style.BRIGHT+"Q"+Style.RESET_ALL
QUE3=Fore.WHITE+Back.BLACK+Style.BRIGHT+"Q"+Style.RESET_ALL
HEALTH=Fore.YELLOW+Back.YELLOW+Style.BRIGHT+"o"+Style.RESET_ALL
