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
    
    
    def makeAction(self, message) :
        """
        Permits to make an action.
        :param: message The message that will be printed before decision
        :return: An int describing the decision.
        """
        return int(input(message))
    

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