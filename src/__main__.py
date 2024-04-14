from DeepRL.opponent.RandomPlayer import RandomPlayer
from DeepRL.Board import Board

def main() :
    board = Board()
    player = RandomPlayer('X')
    x = player.makeAction("Choose a number between 1 and 3 for the x position.")
    y = player.makeAction("Choose a number between 1 and 3 for the y position.")
    
    print(f'Chosen coordinates (x, y) : ({x}, {y})')
    board.capture(x, y, player)
    
    board.printBoard()


if __name__ == '__main__' :
    main()