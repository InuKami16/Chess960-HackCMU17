from abc import ABCMeta, abstractmethod

class Piece(metaclass = ABCMeta):
    def __init__(self, image):
        self.imageRef = image
    
    @abstractmethod
    def getMoves():
        pass

    @abstractmethod
    def move():
        pass
