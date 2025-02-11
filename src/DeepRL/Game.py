from .Board import Board
from .opponent.Opponent import Opponent

class Game() :
    """ This class represents Game instances """
    
    
    def __init__(self, board, opp1, opp2, verbose = True) :
        """
        Creates a new game
        :param: board The board where the game will take place
        :param: opp1 The first opponent
        :param: opp2 The second opponent
        :param: verbose True by default, this tells if board has to be printed when game is played.
        """
        self.__BOARD = board
        self.__OPPONENT1 = opp1
        self.__OPPONENT2 = opp2
        self.__activeOpponent = opp1
        self.__notActiveOpponent = opp2
        self.verbose = verbose
        self.diminFactor = 0.8
        
        self.__opp1History = []
        self.__opp2History = []
    
    
    def changeActiveOpponent(self) :
        """
        Switches the active opponent of the game.
        The active opponent is the one who will capture a case next time a round is played.
        """
        if self.__activeOpponent == self.__OPPONENT1 :
            self.__activeOpponent = self.__OPPONENT2
            self.__notActiveOpponent = self.__OPPONENT1
        else :
            self.__activeOpponent = self.__OPPONENT1
            self.__notActiveOpponent = self.__OPPONENT2
    
    
    
    def play(self) :
        """
        This method permits to run the game.
        Rewards are managed to make sure both AIs can train at the same time by playing against each other.
        """
        firstRoundFinished = False
        
        while not self.isFinished() :
            
            if self.verbose :
                print("")
                self.__BOARD.printBoard()
                print("")
            
            state = self.getState()
            action, reward = self.play_one_round()
            self.addToHistory((state, action), self.__activeOpponent)

            self.changeActiveOpponent()
        
        # Needs to print the final board.
        if self.verbose :
            print("")
            self.__BOARD.printBoard()
            print("")
        self.opponentLearnsFromGameHistory()
    


    def play_one_round(self) :
        """
        The active opponent plays once.
        """
        if not self.isFinished() : 								# Cannot play if game is already finished.
            state = self.getState()
            action = self.__activeOpponent.makeAction(state)	# Active agent choose which action to make
            reward, newState = self.__step(action)			# The game verifies action's integrity (avoiding cheat), applies the action and returns the immediate reward.
            
            while reward == -100 :							# Active opponent tried to cheat, invalid move, game's state has not changed.
                self.__activeOpponent.learn(state, action, reward)	# Learns not to cheat.
                # Active opponent makes a new move
                action = self.__activeOpponent.makeAction(state)
                reward, newState = self.__step(action)
            
            return action, reward
        return None, None





    def addToHistory(self, record, opponent) :
        """
        Adds the recod : (state, action) to game history of the opponent.
        """
        if opponent == self.__OPPONENT1 :
            self.__opp1History.append(record)
        else :
            self.__opp2History.append(record)


    
    def opponentLearnsFromGameHistory(self) :
        """
        Depending on the result of the game,
        both opponents learn depending on what they have done during this game.
        """
        winner = self.getWinner()
        if winner == self.__OPPONENT1 :
            reward = 1
        elif winner == self.__OPPONENT2 :
            reward = -1
        else :
            reward = 0
        
        if self.__OPPONENT1.trainingMode :
            n = len(self.__opp1History)
            for record in self.__opp1History :
                n -= 1
                self.__OPPONENT1.learn(record[0], record[1], reward * (self.diminFactor**n))
        
        reward *= -1			# If opponent1 won/lost then opponent2 lost/won it reverses rewards.
        
        if self.__OPPONENT2.trainingMode :
            n = len(self.__opp2History)
            for record in self.__opp2History :
                n -= 1
                self.__OPPONENT2.learn(record[0], record[1], reward * (self.diminFactor**n))

    
    
    def isFinished(self) :
        """
        Verifies if the game is finished
        :returns: True if the game is finished, False otherwise
        """
        winnerExists = not self.getWinner() is None	# Verifies if somebody has won
        if winnerExists:
            return True
        else :										# Verifies that not all cases are captured
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
        return self.__BOARD.copyGrid()
    
    
    def __step(self, action) :
        """
        Plays the action, calculates the reward and the final state
        :param: action The action that has been made by the active opponent
        :returns: reward The reward given by the env to the opponent
        :returns: state The state of the game after the action has been done.
        """
        x, y = (action % 3, action // 3)
        
        if self.__BOARD.getCell(x, y).getOwner() is not None :
            if self.verbose :
                print("INVALID MOVE")
            return -100, self.getState()
        
        self.__BOARD.capture(x, y, self.__activeOpponent)
        
        return 0, self.getState()
        
    
    
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
