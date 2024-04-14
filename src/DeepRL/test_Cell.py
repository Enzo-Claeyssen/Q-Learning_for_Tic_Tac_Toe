import unittest
from src.DeepRL.Cell import Cell
from src.DeepRL.opponent.Opponent import Opponent

class TestCell(unittest.TestCase) :
    
    def setUp(self) :
        self.cell = Cell()
    
    def test_setAndGetOwner(self) :
        opp = Opponent('X')
        self.cell.setOwner(opp)
        self.assertEqual(opp, self.cell.getOwner())
        