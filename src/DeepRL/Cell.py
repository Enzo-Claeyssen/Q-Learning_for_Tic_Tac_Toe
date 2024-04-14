from src.DeepRL.opponent.Opponent import Opponent

class Cell() :
    """ This class represents cells used within the board. """
    
    def __init__(self) :
        """ Creates a new cell """
        self.__owner = None
    
    def setOwner(self, opp) :
        """ Sets the owner of the cell if the cell isn't already captured. """
        if(self.__owner == None) :
            self.__owner = opp
    
    def getOwner(self) :
        """ Retrieves the owner of this cell """
        return self.__owner
    
    def printCell(self) :
        """ Prints the symbole of the owner """
        pass
