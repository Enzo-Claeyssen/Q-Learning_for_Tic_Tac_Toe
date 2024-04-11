from abc import abstractmethod

class Opponent() :
    
    @abstractmethod
    def makeAction(self, message) :
        pass