from abc import abstractmethod

class Opponent() :
    """This class represents opponents playing games."""
    
    def __init__(self, symbole) :
        """
        Creates a new opponent
        :Param: symbole The symbole used to represent cells capture by this opponent
        """
        self.__SYMBOLE = symbole
    
    
    def getSymbole(self) :
        """ Retrieves the symbole of an opponent """
        return self.__SYMBOLE
    
    
    @abstractmethod
    def makeAction(self, message) :
        """
        This method permits an opponent to make a decision
        :Params: message the string printed to explain the choice
        :Return: An int representing the choice made.
        """
        pass
    
    
    @abstractmethod
    def learn(self, state, action, reward, newState) :
        """
        This method makes the agent learns based on what has just happened.
        If the agent isn't capable of learning then it won't do anything.
        :param: state The initial state where the opponent played.
        :param: action The action realised by the opponent
        :param: reward The immediate reward obtained by the opponent
        :param: newState The state of the game after the second opponent played
        """
        pass
    
    
    def __processState(state) :
        """
        Transforms the classical representation of a state as a unique integer.
        This makes some manipulations easier.
        :param: state The classical representation of the state as a grid of cell.
        :returns: A unique integer identifying this particular state.
        """
        pass
