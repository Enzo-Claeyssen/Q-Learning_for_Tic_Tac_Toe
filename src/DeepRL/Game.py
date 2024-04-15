from .Board import Board
from .opponent.Opponent import Opponent

class Game() :
    """ This class represents Game instances """
    
    def __init__(self, board, opp1, opp2) :
        """
        Creates a new game
        :param: board The board where the game will take place
        :param: opp1 The first opponent
        :param: opp2 The second opponent
        """
        self.__BOARD = board
        self.__OPPONENT1 = opp1
        self.__OPPONENT2 = opp2
    
    
    def isFinished(self) :
        """
        Verifies if the game is finished
        :returns: True if the game is finished, False otherwise
        """
        winnerExists = not self.getWinner() is None
        if winnerExists:
            return True
        else :
            for y in range(3) :
                for x in range(3) :
                    if self.__BOARD.getCell(x, y).getOwner() is None :
                        return False
            return True
    
    
    def getWinner(self) :
        """
        Retrieves the winner of the game
        :returns: The opponent object representing the winner
        """
        owner_grid = [[self.__BOARD.getCell(x, y).getOwner() for x in range(3)] for y in range(3)]
        
        equality_verification = [[(0, 0), (0, 1), (0, 2)], # This contains a set of coordinates corresponding to a line
                                 [(1, 0), (1, 1), (1, 2)],
                                 [(2, 0), (2, 1), (2, 2)],
                                 [(0, 0), (1, 0), (2, 0)],
                                 [(0, 1), (1, 1), (2, 1)],
                                 [(0, 2), (1, 2), (2, 2)],
                                 [(0, 0), (1, 1), (2, 2)],
                                 [(2, 0), (1, 1), (0, 2)]]
        numberOfNotCaptured = 0
        for case in equality_verification :
            aligned = True
            x, y = case[0]
            opp = self.__BOARD.getCell(x, y).getOwner()
            if not opp is None :
                for (x, y) in case[1:] :
                    if opp != self.__BOARD.getCell(x, y).getOwner() :
                        aligned = False
                if aligned :
                    return opp
        return None
