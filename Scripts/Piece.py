from abc import ABCMeta, abstractmethod
from Board import *

class Piece(metaclass = ABCMeta):

    #side = 0 is white
    #side = 1 is black

    def __init__(self, position, imageDir, side):
        self.__position = position
        self.__image = imageDir
        self.__side = side
    
    @abstractmethod
    def getMoves(self):
        pass
    
    def getPosition(self):
        return self.__position

    def getImage(self):
        return self.__image

    def getSide(self):
        return self.__side

    def __str__(self):
        return str(self.__position) + '\t' + str(self.__side)

class Pawn(Piece):
    def __init__(self, position, imageDir, side):
        super().__init__(position, imageDir, side)
        self.__isFirstTurn = True

    def getMoves(self):
        pos0 = super().getPosition()[0]
        pos1 = super().getPosition()[1]
        if self.__isFirstTurn:
            return [[pos0 + (-1)**(super().getSide() + 1), pos1],
                    [pos0 + 2 * (-1)**(super().getSide() + 1), pos1]
                    ]
        else:
            moves = [[pos0 + (-1)**(super().getSide() + 1), pos1],
                    [pos0 + (-1)**(super().getSide() + 1), pos1 + 1],
                    [pos0 + (-1)**(super().getSide() + 1), pos1 - 1]
                    ]
            i = 0
            while(i < len(moves)):
                if not(0 <= moves[i][0] <= 7) or not(0 <= moves[i][1] <= 7):
                    del moves[i]
                else:
                    i += 1
        return moves
    
    def changeIsFirstTurn():
        self.__isFirstTurn = False

    def __str__(self):
        return super().__str__() + 'Pawn'

class Bishop(Piece):
    def __init__(self, position, imageDir, side):
        super().__init__(position, imageDir, side)

    def getMoves(self):
        pos0 = super().getPosition()[0]
        pos1 = super().getPosition()[1]
        i = pos0
        j = pos1
        moves = []
        while (0 <= i + 1 <= 7 and 0 <= j + 1 <= 7):
            moves.append([i + 1, j + 1])
            i += 1
            j += 1
        i = pos0
        j = pos1
        while (0 <= i + 1 <= 7 and 0 <= j - 1 <= 7):
            moves.append([i + 1, j - 1])
            i += 1
            j -= 1
        i = pos0
        j = pos1
        while (0 <= i - 1 <= 7 and 0 <= j + 1 <= 7):
            moves.append([i - 1, j + 1])
            i -= 1
            j += 1
        i = pos0
        j = pos1
        while (0 <= i - 1 <= 7 and 0 <= j - 1 <= 7):
            moves.append([i - 1, j - 1])
            i -= 1
            j -= 1
        return moves

    def __str__(self):
        return super().__str__() + 'Bishop'
    
class King(Piece):
    def __init__(self, position, imageDir, side):
        super().__init__(position, imageDir, side)

    def getMoves(self):
        pos0 = super().getPosition()[0]
        pos1 = super().getPosition()[1]
        moves = [[pos0 + 1, pos1 + 1],
                [pos0, pos1 + 1],
                [pos0 - 1, pos1 + 1],
                [pos0 + 1, pos1],
                [pos0 - 1, pos1],
                [pos0 + 1, pos1 - 1],
                [pos0, pos1 - 1],
                [pos0 - 1, pos1 - 1]
                ]
        i = 0
        while(i < len(moves)):
            if not(0 <= moves[i][0] <= 7) or not(0 <= moves[i][1] <= 7):
                del moves[i]
            else:
                i += 1
        return moves

    def __str__(self):
        return super().__str__() + 'King'
    
class Queen(Piece):
    def __init__(self, position, imageDir, side):
        super().__init__(position, imageDir, side)

    def getMoves(self):
        pos0 = super().getPosition()[0]
        pos1 = super().getPosition()[1]
        i = pos0
        j = pos1
        moves = []
        while (0 <= i + 1 <= 7):
            moves.append([i + 1, j])
            i += 1
        i = pos0
        while (0 <= i - 1 <= 7):
            moves.append([i - 1, j])
            i -= 1
        while (0 <= j + 1 <= 7):
            moves.append([i, j + 1])
            j += 1
        j = pos1
        while (0 <= j - 1 <= 7):
            moves.append([i, j - 1])
            j -= 1
        i = pos0
        j = pos1
        while (0 <= i + 1 <= 7 and 0 <= j + 1 <= 7):
            moves.append([i + 1, j + 1])
            i += 1
            j += 1
        i = pos0
        j = pos1
        while (0 <= i + 1 <= 7 and 0 <= j - 1 <= 7):
            moves.append([i + 1, j - 1])
            i += 1
            j -= 1
        i = pos0
        j = pos1
        while (0 <= i - 1 <= 7 and 0 <= j + 1 <= 7):
            moves.append([i - 1, j + 1])
            i -= 1
            j += 1
        i = pos0
        j = pos1
        while (0 <= i - 1 <= 7 and 0 <= j - 1 <= 7):
            moves.append([i - 1, j - 1])
            i -= 1
            j -= 1
        return moves

    def __str__(self):
        return super().__str__() + 'Queen'
    
class Knight(Piece):
    def __init__(self, position, imageDir, side):
        super().__init__(position, imageDir, side)

    def getMoves(self):
        pos0 = super().getPosition()[0]
        pos1 = super().getPosition()[1]
        moves = [[pos0 + 2, pos1 + 1],
                [pos0 + 2, pos1 - 1],
                [pos0 + 1, pos1 + 2],
                [pos0 + 1, pos1 - 2],
                [pos0 - 1, pos1 + 2],
                [pos0 - 1, pos1 - 2],
                [pos0 - 2, pos1 + 1],
                [pos0 - 2, pos1 - 1]
                ]
        i = 0
        while(i < len(moves)):
            if not(0 <= moves[i][0] <= 7) or not(0 <= moves[i][1] <= 7):
                del moves[i]
            else:
                i += 1
        return moves

    def __str__(self):
        return super().__str__() + 'Knight'
    
class Rook(Piece):
    def __init__(self, position, imageDir, side):
        super().__init__(position, imageDir, side)

    def getMoves(self):
        pos0 = super().getPosition()[0]
        pos1 = super().getPosition()[1]
        i = pos0
        j = pos1
        moves = []
        while (0 <= i + 1 <= 7):
            moves.append([i + 1, j])
            i += 1
        i = pos0
        while (0 <= i - 1 <= 7):
            moves.append([i - 1, j])
            i -= 1
        while (0 <= j + 1 <= 7):
            moves.append([i, j + 1])
            j += 1
        j = pos1
        while (0 <= j - 1 <= 7):
            moves.append([i, j - 1])
            j -= 1
        return moves

    def __str__(self):
        return super().__str__() + 'Rook'
