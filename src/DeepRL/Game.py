from .Board import Board
from .opponent.Opponent import Opponent

class Game() :
    """ This class represents Game instances """
    
    def __init__(self, opp1, opp2) :
        """
        Creates a new game
        :param: opp1 The first opponent
        :param: opp2 The second opponent
        """
        self.__BOARD = Board()
        self.__OPPONENT1 = opp1
        self.__OPPONENT2 = opp2
        self.__activeOpponent = opp1
    
    
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
        self.__activeOpponent = opp1
    
    
    def play(self) :
        """
        This method permits to run the game.
        """
        while(not self.isFinished()) :
            own_tmp = self.__OPPONENT1
            while own_tmp != None :
                x = self.__OPPONENT1.makeAction("Choose a column (0 to 2)")
                y = self.__OPPONENT1.makeAction("Choose a row (0 to 2)")
                own_tmp = self.__BOARD.getCell(x, y).getOwner()
            self.__BOARD.capture(x, y, self.__OPPONENT1)
            self.__BOARD.printBoard()
            
            if not self.isFinished() :
                own_tmp = self.__OPPONENT2
                while own_tmp != None :
                    x = self.__OPPONENT2.makeAction("Choose a column (0 to 2)")
                    y = self.__OPPONENT2.makeAction("Choose a row (0 to 2)")
                    own_tmp = self.__BOARD.getCell(x, y).getOwner()
                self.__BOARD.capture(x, y, self.__OPPONENT2)
                self.__BOARD.printBoard()
    
    
    def newPlay(self) :
        """
        This method permits to run the game.
        Rewards are managed to make sure both AIs can train at the same time by playing against each other.
        """
        # Initialize first round
        firstRoundFinished = False
        state1 = self.getState()
        
        while True :
            
            self.__BOARD.printBoard()
            
            if not self.isFinished() :
                # Opponent 1 plays
                self.__activeOpponent = self.__OPPONENT1
                action1 = self.__activeOpponent.makeAction(state1)
                reward1, state2 = self.step(action1)
                # Play until choosing a valid action
                while reward1 == -100 :
                    # Agent learns he took an invalid action
                    self.__activeOpponent.learn(state1, action1, reward1, state2)
                    # Plays once again
                    action1 = self.__activeOpponent.makeAction(state1)
                    reward1, state2 = self.step(action1)
                # If opp2 played then he learns
                if firstRoundFinished :
                    self.__OPPONENT2.learn(state2, action2, -1 * reward1, state1)
            else :
                # Opponent 2 finished the game
                self.__OPPONENT2.learn(state2, action2, reward2, state1)
                break
            
            firstRoundFinished = True
            self.__BOARD.printBoard()
            
            if not self.isFinished() :
                # Opponent 2 plays
                self.__activeOpponent = self.__OPPONENT2
                action2 = self.__activeOpponent.makeAction(state2)
                reward2, state1 = self.step(action2)
                # Play until choosing a valid action
                while reward2 == -100 :
                    # Agent learns he took an invalid action
                    self.__activeOpponent.learn(state2, action2, reward2, state1)
                    # Plays once again
                    action2 = self.__activeOpponent.makeAction(state2)
                    reward2, state1 = self.step(action2)
                # At the end of Opp2's turn Opp1 learns
                self.__OPPONENT1.learn(state1, action1, -1 * reward2, state2)
            else :
                # Opponent 1 finished the game
                self.__OPPONENT1.learn(state1, action1, reward1, state2)
                break
        
        #End of the game
    
    
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
    
    def getState(self) :
        """
        Retrieves the state of the game
        :returns: Board's representation as a list of list of Cell
        """
        #TODO
        pass
    
    
    def __step(self, action) :
        """
        Plays the action, calculates the reward and the final state
        :param: action The action that has been made by the active opponent
        :returns: reward The reward given by the env to the opponent
        :returns: state The state of the game after the action has been done.
        """
        # TODO
        pass
    
    
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
