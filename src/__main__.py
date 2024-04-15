from DeepRL.Game import Game
from DeepRL.opponent.RandomPlayer import RandomPlayer
from DeepRL.Board import Board

def main() :
    board = Board()
    player1 = RandomPlayer('X')
    player2 = RandomPlayer('O')
    game = Game(board, player1, player2)
    
    while(not game.isFinished()) :
        board.capture(player1.makeAction("X player's turn"), player1.makeAction(""), player1)
        board.printBoard()
        if(not game.isFinished()) :
            board.capture(player2.makeAction("O player's turn"), player2.makeAction(""), player2)
            board.printBoard()
    
    winner = game.getWinner()
    if winner == player1 :
        print('X player wins !')
    elif winner == player2 :
        print('O player wins !')
    else :
        print('Draw !')
    
    
    
    


if __name__ == '__main__' :
    main()