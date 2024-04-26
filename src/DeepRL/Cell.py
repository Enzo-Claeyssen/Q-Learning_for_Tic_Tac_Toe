from .opponent.Opponent import Opponent

class Cell() :
    """ This class represents cells used within the board. """
    
    def __init__(self) :
        """ Creates a new cell """
        self.__owner = None
    
    def getCopy(self) :
        """
        Creates an independant copy of this cell
        :returns: Copy of this but as a new instance of this class
        """
        copy = Cell()
        copy.setOwner(self.getOwner())
        return copy
    
    def setOwner(self, opp) :
        """ Sets the owner of the cell if the cell isn't already captured. """
        if(self.__owner == None) :
            self.__owner = opp
    
    def getOwner(self) :
        """ Retrieves the owner of this cell """
        return self.__owner
    
    def getCellRepresentation(self) :
        """ Returns the symbole of the owner """
        opp = self.getOwner()
        if(opp is None) :
            return ' '
        else :
            return opp.getSymbole()
