from DeepRL.Game import Game
from DeepRL.opponent.Player import Player
from DeepRL.opponent.RandomPlayer import RandomPlayer
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
    navigate_mainMenu()

def printWinner() :
    winner = GAME.getWinner()
    if not winner is None :
        print(f'{winner.getSymbole()} player wins !')
    else :
        print('Draw !')



def main() :
    navigate_mainMenu()


if __name__ == '__main__' :
    main()
