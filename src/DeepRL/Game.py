from .Board import Board
from .opponent.Opponent import Opponent

class Game() :
    """ This class represents Game instances """
    
    def __init__(board, opp1, opp2) :
        """
        Creates a new game
        :param: board The board where the game will take place
        :param: opp1 The first opponent
        :param: opp2 The second opponent
        """
        pass
    
    
    def isFinished() :
        """
        Verifies if the game is finished
        :returns: True if the game is finished, False otherwise
        """
        pass
    
    
    def getWinner() :
        """
        Retrieves the winner of the game
        :returns: The opponent object representing the winner
        """
        pass
