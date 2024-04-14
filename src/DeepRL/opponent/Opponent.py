from abc import abstractmethod

class Opponent() :
    """This class represents opponents playing games."""
    
    def __init__(self, symbole) :
        """
        Creates a new opponent
        :Param: symbole The symbole used to represent cells capture by this opponent
        """
        self.__SYMBOLE = symbole
    
    
    def getSymbole(self) :
        """ Retrieves the symbole of an opponent """
        return self.__SYMBOLE
    
    
    @abstractmethod
    def makeAction(self, message) :
        """
            This method permits an opponent to make a decision
            :Params: message the string printed to explain the choice
            :Return: An int representing the choice made.
        """
        pass
