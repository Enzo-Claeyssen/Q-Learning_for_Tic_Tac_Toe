import unittest
from src.DeepRL.opponent.RandomPlayer import RandomPlayer
from src.DeepRL.opponent.test_Opponent import testOpponent

class testRandomPlayer(unittest.TestCase, testOpponent) :
    
    
    def setUp(self) :
        self.opp = RandomPlayer('X')
    
    
    def testGetSymbole(self) :
        self.assertEqual('X', self.opp.getSymbole())