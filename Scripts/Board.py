from random import *

class Board:
    def __init__(self):
        self.__colorBoard = [[(i + j) % 2 for j in range(8)] for i in range(8)]
        self.__gameBoard = [[0 for j in range(8)] for i in range(8)]
        self.__backRow = [2, 3, 4, 6, 5, 4, 3, 2]
        
    def getColorBoard(self):
        return self.__colorBoard

    def getGameBoard(self):
        return self.__gameBoard

    def initGameBoard(self):
        self.__gameBoard[1] = [1 for i in range(8)]
        self.__gameBoard[len(self.__gameBoard) - 2] = [1 for i in range(8)]
        shuffle(self.__backRow)
        self.__gameBoard[0] = self.__backRow
        self.__gameBoard[len(self.__gameBoard) - 1] = self.__backRow

    def move(self, piece, position):
        self.__gameBoard[position[0]][position[1]] = self.__gameBoard[piece[0]][piece[1]]
        self.__gameBoard[piece[0]][piece[1]] = 0
