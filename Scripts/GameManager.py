from random import *
from Board import *

class GameManager:

    #0 is white
    #1 is black
    
    def __init__(self):
        self.__turnCount = 0
        self.__turn = randint(0,1)
        self.__board = Board()
        self.__board.initGameBoard()

    def getTurnCount(self):
        return self.__turnCount

    def getTurn(self):
        return self.__turn
    
    def getBoard(self):
        return self.__board

    

    
