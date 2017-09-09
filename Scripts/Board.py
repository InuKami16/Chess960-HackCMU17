from random import *
from Piece import *
import pprint
import copy

class Board:
    def __init__(self):
        self.__colorBoard = [[(i + j) % 2 for j in range(8)] for i in range(8)]
        self.__gameBoard = [[0 for j in range(8)] for i in range(8)]
        self.__backRow = [2, 3, 4, 6, 5, 4, 3, 2]
        self.initGameBoard()
        
    def getColorBoard(self):
        return self.__colorBoard

    def getGameBoard(self):
        return self.__gameBoard

    def initGameBoard(self):
        self.__gameBoard[1] = [1 for i in range(8)]
        self.__gameBoard[len(self.__gameBoard) - 2] = [1 for i in range(8)]
        shuffle(self.__backRow)
        self.__gameBoard[0] = copy.copy(self.__backRow)
        self.__gameBoard[len(self.__gameBoard) - 1] = copy.copy(self.__backRow)        
        pprint.pprint(self.__gameBoard)
        for i in range(8):
            for j in range(8):
                print("Board position", i, j, self.__gameBoard[i][j])
                lencase = i < (len(self.__gameBoard) / 2)
                print("Lencase", lencase)                
                if self.__gameBoard[i][j] == 1:
                        self.__gameBoard[i][j] = Pawn([i, j], 'pawn.png', int(lencase))
                elif self.__gameBoard[i][j] == 2:
                        self.__gameBoard[i][j] = Rook([i, j], 'rook.png', int(lencase))
                elif self.__gameBoard[i][j] == 3:
                        self.__gameBoard[i][j] = Knight([i, j], 'knight.png', int(lencase))
                elif self.__gameBoard[i][j] == 4:
                        self.__gameBoard[i][j] = Bishop([i, j], 'bishop.png', int(lencase))
                elif self.__gameBoard[i][j] == 5:
                        self.__gameBoard[i][j] = King([i, j], 'king.png', int(lencase))
                elif self.__gameBoard[i][j] == 6:
                        self.__gameBoard[i][j] = Queen([i, j], 'queen.png', int(lencase))
                                        
    def move(self, piece, position):
        self.__gameBoard[position[0]][position[1]] = self.__gameBoard[piece[0]][piece[1]]
        self.__gameBoard[piece[0]][piece[1]] = 0
