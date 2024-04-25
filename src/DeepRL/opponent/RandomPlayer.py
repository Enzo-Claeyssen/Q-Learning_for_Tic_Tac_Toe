from .Opponent import Opponent
import random

class RandomPlayer(Opponent) :
    """
    This class represents a player who plays randomly.
    """
    
    def __init__(self, symbole) :
        """
        Creates a new RandomPlayer
        :Param: symbole The symbole associated with cells captured by this opponent
        """
        super().__init__(symbole)
    
    def makeAction(self, message) :
        """
        Permits a randomPlayer to make a random choice.
        Parameters :
            message : The message which is printed to permit making a choice
        Returns :
            A random integer.
        """
        print(message)
        return random.randint(0, 2)
    
    
    def learn(state, action, reward, newState) :
        """
        This method makes the agent learns based on what has just happened.
        If the agent isn't capable of learning then it won't do anything.
        :param: state The initial state where the opponent played.
        :param: action The action realised by the opponent
        :param: reward The immediate reward obtained by the opponent
        :param: newState The state of the game after the second opponent played
        """
        pass
