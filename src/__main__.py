from DeepRL.Game import Game
from DeepRL.opponent.Player import Player
from DeepRL.opponent.RandomPlayer import RandomPlayer
from DeepRL.opponent.QLearningTTT import QLearningTTT
from DeepRL.opponent.DQN import DQN
from DeepRL.Board import Board
from tqdm import tqdm


# Global variables
OPP1 = RandomPlayer('X')
OPP2 = RandomPlayer('O')
GAME = Game(Board(), OPP1, OPP2)



def navigate_mainMenu() :
    print("---Main Menu---")
    print("Type the corresponding number to make a choice.")
    x = -1
    while(not (x >= 0 and x <= 2)) :
        print("0 : New Game")
        print("1 : Training")
        print("2 : Import/Export")
        x = int(input("Your choice : "))
    
    match x :
        case 0 :
            navigate_gameSettings()
        case 1 :
            navigate_trainingMenu()
        case 2 :
            navigate_importMenu()


def navigate_gameSettings() :
    global OPP1
    global OPP2
    global GAME
    print("--- Game Setup ---")
    x = -1
    while(not(x >= 0 and x <= 2)) :
        print("0 : Player vs Player")
        print("1 : Player vs AI")
        print("2 : AI vs AI")
        x = int(input("Your choice : "))
    
    match x :
        case 0 :
            OPP1 = Player('X')
            OPP2 = Player('O')
            
        case 1 :
            symbole = chooseSymbole()
            if symbole == 'X' :
                opponent = chooseOpponent('O')
                OPP1 = Player('X')
                OPP2 = opponent
            else :
                opponent = chooseOpponent('X')
                OPP1 = opponent
                OPP2 = Player('O')
        
        case 2 :
            print("Creating opponent 1 : ")
            opponent1 = chooseOpponent('X')
            print("Creating opponent 2 : ")
            opponent2 = chooseOpponent('O')
            OPP1 = opponent1
            OPP2 = opponent2
    
    runGame()
    navigate_mainMenu()


def navigate_trainingMenu() :
    global OPP1
    global OPP2
    print("---Training Menu---")
    
    print("Choose which AI to train : ")
    print("0 : Q-LearningTTT")
    print("1 : DQN")
    
    x = int(input("Input here : "))
    match x :
        case 0 :
            OPP1 = QLearningTTT('X', True)
            OPP2 = QLearningTTT('O', True)
        case 1 :
            OPP1 = DQN('X', True)
            OPP2 = DQN('O', True)
    
    
    trainingGames = int(input("Enter here number of training games : "))
    for i in tqdm(range(trainingGames), desc = "Training...") :
        runGame(False)
        OPP1.decayEpsilon()
        OPP2.decayEpsilon()
        
    print("Training Completed")
    navigate_mainMenu()

def navigate_importMenu() :
    print('---Import/Export---')
    print('0 : Reset')
    print('1 : Import')
    print('2 : Export')
    x = int(input('Enter here : '))
    
    match x :
        case 0 :
            QLearningTTT.resetQTable()
        
        case 1 :
            QLearningTTT.importQTable()
        
        case 2:
            QLearningTTT.exportQTable()
    
    navigate_mainMenu()
            


def chooseSymbole() :
    print("Choose your symbole, X player will begin.")
    y = -1
    while(not(y >= 0 and y <= 1)) :
        print("0 : Play as X")
        print("1 : Play as O")
        y = int(input("Your choice : "))
    if y == 0 :
        return 'X'
    else :
        return 'O'

def chooseOpponent(symbole) :
    print("Choose the type of the opponent.")
    print("0 : Random")
    print("1 : Q-LearningTTT")
    print("2 : DQN")
    x = int(input("Enter your choice : "))
    
    match x :
        case 0 :
            return RandomPlayer(symbole)
        
        case 1 :
            return QLearningTTT(symbole, False)
        
        case 2 :
            return DQN(symbole, False)



def runGame(verbose = True) :
    global OPP1
    global OPP2
    global GAME
    GAME = Game(Board(), OPP1, OPP2, verbose)
    GAME.play()
    if verbose :
        printWinner()

def printWinner() :
    winner = GAME.getWinner()
    if not winner is None :
        print(f'{winner.getSymbole()} player wins !')
    else :
        print('Draw !')



def mainExport() :
    global OPP1
    global OPP2
    print("---Training Menu---")
    trainingGames = int(input("Enter here number of training games : "))
    OPP1 = QLearningTTT('X', True)
    OPP2 = QLearningTTT('O', True)
    for i in range(trainingGames) :
        runGame(False)
        OPP1.decayEpsilon()
        OPP2.decayEpsilon()
        
        print(f"{i/trainingGames*100} %")
    print("Training Completed")
    OPP1.exportQTable()

def mainImport() :
    QLearningTTT('X', True).importQTable()
    navigate_mainMenu()




def main() :
    navigate_mainMenu()


if __name__ == '__main__' :
    main()
