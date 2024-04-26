from DeepRL.Game import Game
from DeepRL.opponent.Player import Player
from DeepRL.opponent.RandomPlayer import RandomPlayer
from DeepRL.opponent.QLearningTTT import QLearningTTT
from DeepRL.Board import Board


# Global variables
OPP1 = RandomPlayer('X')
OPP2 = RandomPlayer('O')
GAME = Game(Board(), OPP1, OPP2)



def navigate_mainMenu() :
    print("---Main Menu---")
    print("Type the corresponding number to make a choice.")
    x = -1
    while(not (x >= 0 and x <= 0)) :
        print("0 : New Game")
        x = int(input("Your choice : "))
    if x == 0 :
        navigate_gameSettings()


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
            print("Choose your symbole, X player will begin.")
            
            y = -1
            while(not(y >= 0 and y <= 1)) :
                print("0 : Play as X")
                print("1 : Play as O")
                y = int(input("Your choice : "))
            if y == 0 :
                OPP1 = Player('X')
                OPP2 = RandomPlayer('O')
            else :
                OPP1 = RandomPlayer('X')
                OPP2 = Player('O')
        
        case 2 :
            OPP1 = RandomPlayer('X')
            OPP2 = RandomPlayer('O')
    
    runGame()


def runGame() :
    global OPP1
    global OPP2
    global GAME
    GAME = Game(Board(), OPP1, OPP2)
    GAME.play()
    printWinner()

def printWinner() :
    winner = GAME.getWinner()
    if not winner is None :
        print(f'{winner.getSymbole()} player wins !')
    else :
        print('Draw !')



def main() :
    global OPP1
    global OPP2
    global GAME
    
    print("")
    print("Welcome, this program trains a bot using Q-Learning to play Tic Tac Toe.")
    print("To perform well enough, this bot needs to train by playing games against himself.")
    print("Even after the training, the bot will continue to learn by playing against you.")
    print("Enter below the number of games the bot will play against himself in order to train.")
    print("")
    print("0 - Not trained")
    print("1000 - Easy")
    print("40000 - Medium")
    print("100000 - Impossible")
    trainingGames = int(input("Enter here number of training games : "))
    OPP1 = QLearningTTT('X', True)
    OPP2 = QLearningTTT('O', True)
    for i in range(trainingGames) :
        GAME = Game(Board(), OPP1, OPP2, verbose = False)
        GAME.play()
        
        OPP1.decayEpsilon()
        OPP2.decayEpsilon()
        
        print(f"{i/trainingGames*100} %")
    
    while True :
        print("Choose your symbole, X player will begin.")
                
        y = -1
        while(not(y >= 0 and y <= 1)) :
            print("0 : Play as X")
            print("1 : Play as O")
            y = int(input("Your choice : "))
        if y == 0 :
            OPP1 = Player('X')
            OPP2 = QLearningTTT('O', False)
        else :
            OPP1 = QLearningTTT('X', False)
            OPP2 = Player('O')
        
        runGame()
    
    



def OLD_main() :
    navigate_mainMenu()


if __name__ == '__main__' :
    main()
