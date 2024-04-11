from abc import abstractmethod

class Opponent() :
    """
    This class represents opponents playing games.
    """
    
    @abstractmethod
    def makeAction(self, message) :
        """
        This method permits an opponent to make a decision
        Paramaters :
            message : a string printed to tell which decision has to be made
        Returns :
            an int representing the choice made
        """
        pass