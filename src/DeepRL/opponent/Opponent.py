from abc import abstractmethod

class Opponent() :
    """This class represents opponents playing games."""
    
    def __init__(symbole) :
        pass
    
    
    def getSymbole() :
        pass
    
    
    @abstractmethod
    def makeAction(self, message) :
        """
            This method permits an opponent to make a decision
            :Params: message the string printed to explain the choice
            :Return: An int representing the choice made.
        """
        pass
