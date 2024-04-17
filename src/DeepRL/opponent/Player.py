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
        pass
    
    
    def makeAction(self, message) :
        """
        Permits to make an action.
        :param: message The message that will be printed before decision
        :return: An int describing the decision.
        """
        pass