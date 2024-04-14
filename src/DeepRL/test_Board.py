import unittest
from src.DeepRL.Board import Board
from src.DeepRL.opponent.Opponent import Opponent

class testBoard(unittest.TestCase) :
    
    def setUp(self) :
        self.board = Board()
        self.opp = Opponent('O')
    
    def test_captureAndGetCell(self) :
        self.board.capture(1, 2, self.opp)
        self.assertEqual(self.opp, self.board.getCell(1, 2).getOwner())