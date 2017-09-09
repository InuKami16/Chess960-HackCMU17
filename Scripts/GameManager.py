from random import *
from Board import *

class GameManager:

    #0 is white turn
    #1 is black turn
    
    def __init__(self):
        self.__turn = randint(0,1)
        self.__board = Board()

    def getTurn(self):
        return self.__turn
    
    def getBoard(self):
        return self.__board

    
