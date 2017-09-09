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

    @abstractmethod
    def move(self, position):
        pass
    
    def getPosition(self):
        return self.__position

    def getImage(self):
        return self.__image

class Pawn(Piece):
    def __init__(self, position, imageDir):
        super().__init__(position, imageDir)

    def getMoves(self):
        return 0
    
    def move(self, position):
        
        return 0

class Bishop(Piece):
    def __init__(self, position, imageDir):
        super().__init__(position, imageDir)

    def getMoves(self):
        return 0

    def move(self, position):
        return 0
    
class King(Piece):
    def __init__(self, position, imageDir):
        super().__init__(position, imageDir)

    def getMoves(self):
        return 0

    def move(self, position):
        return 0
    
class Queen(Piece):
    def __init__(self, position, imageDir):
        super().__init__(position, imageDir)

    def getMoves(self):
        return 0

    def move(self, position):
        return 0
    
class Knight(Piece):
    def __init__(self, position, imageDir):
        super().__init__(position, imageDir)

    def getMoves(self):
        return 0

    def move(self, position):
        return 0
    
class Rook(Piece):
    def __init__(self, position, imageDir):
        super().__init__(position, imageDir)

    def getMoves(self):
        return 0

    def move(self, position):
        return 0
