import unittest
from src.DeepRL.Game import Game
from src.DeepRL.Board import Board
from src.DeepRL.opponent.Opponent import Opponent

class testGame(unittest.TestCase) :
    
    def setUp(self) :
        self.opp1 = Opponent('X')
        self.opp2 = Opponent('O')
        self.board = Board()
        self.game = Game(self.board, self.opp1, self.opp2);
    
    def test_isFinishedHonrizontal(self) :
        self.board.capture(0, 0, self.opp1)
        self.board.capture(0, 1, self.opp1)
        self.board.capture(0, 2, self.opp1)
        self.assertTrue(self.game.isFinished())
    
    def test_isFinishedVertical(self) :
        self.board.capture(0, 0, self.opp2)
        self.board.capture(1, 0, self.opp2)
        self.board.capture(2, 0, self.opp2)
        self.assertTrue(self.game.isFinished())
    
    def test_isFinishedDiagonal(self) :
        self.board.capture(0, 0, self.opp1)
        self.board.capture(1, 1, self.opp1)
        self.board.capture(2, 2, self.opp1)
        self.assertTrue(self.game.isFinished())
    
    def test_isFinishedReturnsFalse_RandomPlay(self) :
        self.board.capture(0, 0, self.opp1)
        self.board.capture(0, 1, self.opp2)
        self.board.capture(2, 2, self.opp1)
        self.board.capture(1, 0, self.opp2)
        self.assertFalse(self.game.isFinished())
    
    def test_isFinishedReturnsFalse_LineFilled(self) :
        self.board.capture(0, 0, self.opp1)
        self.board.capture(1, 1, self.opp1)
        self.board.capture(2, 2, self.opp2) # Opp2 blocks the line
        self.assertFalse(self.game.isFinished())
    
    def test_isFinished_Draw(self) :
        self.board.capture(0, 0, self.opp1)
        self.board.capture(0, 1, self.opp2)
        self.board.capture(0, 2, self.opp1)
        self.board.capture(1, 0, self.opp2)
        self.board.capture(1, 1, self.opp1)
        self.board.capture(1, 2, self.opp1)
        self.board.capture(2, 0, self.opp2)
        self.board.capture(2, 1, self.opp1)
        self.board.capture(2, 2, self.opp2)
        self.assertTrue(self.game.isFinished())
    
    
    def test_getWinner_opp1WinsHorizontal(self) :
        self.board.capture(0, 0, self.opp1)
        self.board.capture(0, 1, self.opp1)
        self.board.capture(0, 2, self.opp1)
        self.assertEqual(self.opp1, self.game.getWinner())
    
    def test_getWinner_opp2WinsVertical(self) :
        self.board.capture(0, 0, self.opp2)
        self.board.capture(1, 0, self.opp2)
        self.board.capture(2, 0, self.opp2)
        self.assertEqual(self.opp2, self.game.getWinner())
    
    def test_getWinner_returnsNullNoWinner(self) :
        self.board.capture(0, 0, self.opp1)
        self.board.capture(1, 1, self.opp1)
        self.board.capture(2, 2, self.opp2) # Opp2 blocks the line
        self.assertIsNone(self.game.getWinner())


if __name__ == '__main__' :
    unittest.main()