import unittest
from models import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def roll(self, rolls):
        for roll in rolls:
            self.game.roll(roll)

    def assertResult(self, expected):
        self.assertEqual(self.game.results(), expected)

    def test_gutter(self):
        self.roll([0] * 20)
        self.assertResult([0] * 10)

    def test_spare(self):
        self.roll([3, 7, 6, 4, 1, 3, 5, 5])
        self.assertResult([16, 27, 31, 41])

    def test_strike(self):
        self.roll([10, 5, 3, 10, 10, 10, 3, 5])
        self.assertResult([18, 26, 56, 79, 97, 105])

    def test_open(self):
        self.roll([2, 3, 4, 2, 3, 5])
        self.assertResult([5, 11, 19])

    def test_full(self):
        self.roll([10, 7, 3, 7, 2, 9, 1, 10, 10, 10, 2, 3, 6, 4, 7, 1])
        self.assertResult([20, 37, 46, 66, 96, 118, 133, 138, 155, 163])

    def test_fill(self):
        self.roll([10, 7, 3, 7, 2, 9, 1, 10, 10, 10, 2, 3, 6, 4, 7, 3, 3])
        self.assertResult([20, 37, 46, 66, 96, 118, 133, 138, 155, 168])

    def test_perfect_game(self):
        self.roll([10] * 12)
        self.assertResult([30, 60, 90, 120, 150, 180, 210, 240, 270, 300])

    def test_game_over(self):
        self.roll([1] * 19)
        self.assertFalse(self.game.is_over())
        self.roll([1])
        self.assertTrue(self.game.is_over())
    
    def test_game_over_fill(self):
        self.roll([10] * 11)
        self.assertFalse(self.game.is_over())
        self.roll([10])
        self.assertTrue(self.game.is_over())