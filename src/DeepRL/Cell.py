from src.DeepRL.opponent.Opponent import Opponent

class Cell() :
    """ This class represents cells used within the board. """
    
    def __init__(self) :
        """ Creates a new cell """
        pass
    
    def setOwner(self, opp) :
        """ Sets the owner of the cell if the cell isn't already captured. """
        pass
    
    def getOwner(self) :
        """ Retrieves the owner of this cell """
        pass
    
    def printCell(self) :
        """ Prints the symbole of the owner """
        pass
