from .Opponent import Opponent
import random

class RandomPlayer(Opponent) :
    """
    This class represents a player who plays randomly.
    """ 
    
    def makeAction(self, message) :
        """
        Permits a randomPlayer to make a random choice.
        Parameters :
            message : The message which is printed to permit making a choice
        Returns :
            A random integer.
        """
        print(message)
        return random.randint(1, 3)
