from .Opponent import Opponent

class Player(Opponent) :
    """
    Represent interactive opponents.
    """
    
    def __init__(self, symbole) :
        """
        Creates a new player
        :param: symbole The symbole representing cells of this player
        """
        super().__init__(symbole)
    
    
    def makeAction(self, state) :
        """
        Permits to make an action.
        :param: state The actual state of the game as a grid of Cell
        :return: An int describing the decision.
        """
        x = int(input("Choose the column where you want to play : "))
        y = int(input("Choose the row where you want to play : "))
        return y*3 + x
    

    def learn(self, state, action, reward, newState) :
        """
        This method makes the agent learns based on what has just happened.
        If the agent isn't capable of learning then it won't do anything.
        :param: state The initial state where the opponent played.
        :param: action The action realised by the opponent
        :param: reward The immediate reward obtained by the opponent
        :param: newState The state of the game after the second opponent played
        """
        # Does Nothing