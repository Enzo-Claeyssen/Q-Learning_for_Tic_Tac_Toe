from DeepRL.Game import Game
from DeepRL.opponent.RandomPlayer import RandomPlayer
from DeepRL.Board import Board

def main() :
    board = Board()
    player1 = RandomPlayer('X')
    player2 = RandomPlayer('O')
    game = Game(board, player1, player2)
    
    game.play()
    
    winner = game.getWinner()
    if winner == player1 :
        print('X player wins !')
    elif winner == player2 :
        print('O player wins !')
    else :
        print('Draw !')
    
    
    
    


if __name__ == '__main__' :
    main()