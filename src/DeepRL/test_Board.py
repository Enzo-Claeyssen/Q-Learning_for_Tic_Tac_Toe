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
    
    def test_copyGrid(self) :
        opp1 = Opponent('X')
        opp2 = Opponent('O')
        self.board.capture(0, 0, opp1)
        self.board.capture(1, 1, opp2)
        self.board.capture(1, 2, opp1)
        
        grid = self.board.copyGrid()
        self.assertEqual(opp1, self.board.getCell(0, 0).getOwner())
        self.assertEqual(opp2, self.board.getCell(1, 1).getOwner())
        self.assertEqual(opp1, self.board.getCell(1, 2).getOwner())
        
        for x in range(3) :
            for y in range(3) :
                if (x, y) != (0, 0) and (x, y) != (1, 1) and (x, y) != (1, 2) :
                    self.assertIsNone(self.board.getCell(x, y).getOwner())
    


if __name__ == '__main__' :
    unittest.main()