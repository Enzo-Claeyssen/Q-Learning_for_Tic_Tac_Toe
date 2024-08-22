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
    def makeAction(self, state) :
        """
        This method permits an opponent to make a decision
        :Params: state The actual state of the game as a grid of Cell
        :Return: An int representing the choice made.
        """
        pass
    
    
    @abstractmethod
    def learn(self, state, action, reward) :
        """
        This method makes the agent learns based on what has just happened.
        If the agent isn't capable of learning then it won't do anything.
        :param: state The initial state where the opponent played.
        :param: action The action realised by the opponent
        :param: reward The immediate reward obtained by the opponent
        :param: newState The state of the game after the second opponent played
        """
        pass
    
    
    def _processState(self, state) :
        """
        Transforms the classical representation of a state as a unique integer.
        This makes some manipulations easier.
        :param: state The classical representation of the state as a grid of cell.
        :returns: A unique integer identifying this particular state.
        """
        sum = 0
        for y in range(3) :
            for x in range(3) :
                cell = state[y][x]
                owner = cell.getOwner()
                
                if owner is not None :
                    if owner == self :
                        sum += 3**(3*y+x)
                    else :
                        sum += (3**(3*y+x)) * 2
        return sum
    
    
    def _linearState(self, state) :
        newState = []
        for y in range(3) :
            for x in range(3) :
                cell = state[y][x]
                owner = cell.getOwner()
                
                if owner is not None :
                    if owner == self :
                        newState.append(1)
                    else :
                        newState.append(-1)
                else :
                    newState.append(0)
        return newState
                
                
