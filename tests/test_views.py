import unittest
from views import *

class TestScoreView(unittest.TestCase):

    def test_score_board(self):
        board = [2, 8, 1, 5, 10]
        self.assertEqual(score_board(board),
            ("\nYour Score:\n"
            "Frame 1: 2\n"
            "Frame 2: 8\n"
            "Frame 3: 1\n"
            "Frame 4: 5\n"
            "Frame 5: 10\n")
        )
    