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
    
    def test_ownerIsNotSetWhenCellAlreadyCaptured(self) :
        opp = Opponent('X')
        opp2 = Opponent('O')
        self.cell.setOwner(opp)
        self.cell.setOwner(opp2)
        self.assertEqual(opp, self.cell.getOwner())
