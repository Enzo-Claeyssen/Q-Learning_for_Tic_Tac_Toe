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
        self.trainingMode = False
    
    
    def makeAction(self, state) :
        """
        Permits to make an action.
        :param: state The actual state of the game as a grid of Cell
        :return: An int describing the decision.
        """
        str_x = input("Choose the row where you want to play : ")
        while not(str_x.isdigit()) :
            print("Invalid, try again.")
            str_x = input("Choose the row where you want to play : ")
        
        str_y = input("Choose the column where you want to play : ")
        while not(str_y.isdigit()) :
            print("Invalid, try again.")
            str_y = input("Choose the column where you want to play : ")
        
        x = int(str_x)
        y = int(str_y)
        
        return x*3 + y
    

    def learn(self, state, action, reward) :
        """
        This method makes the agent learns based on what has just happened.
        If the agent isn't capable of learning then it won't do anything.
        :param: state The initial state where the opponent played.
        :param: action The action realised by the opponent
        :param: reward The immediate reward obtained by the opponent
        :param: newState The state of the game after the second opponent played
        """
        # Does Nothing