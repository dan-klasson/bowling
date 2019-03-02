import unittest
from unittest.mock import patch
from models import Game
from controllers import GameController
import io

class TestController(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, stdout):
        game = GameController()
        try:
            game.run()
        except StopIteration:
            pass
        self.assertIn(expected_output, stdout.getvalue())

    @patch('builtins.input', side_effect=['5', '3', '10'])
    def test_valid_play(self, input):
        self.assert_stdout('Frame 1: 8\nFrame 2: 18') 
        
    @patch('builtins.input', side_effect=['123'])
    def test_invalid_input(self, input):
        self.assert_stdout('Enter digits between 0 and 10')

    @patch('builtins.input', side_effect=['7', '5'])
    def test_invalid_input_second(self, input):
        self.assert_stdout('Enter digits between 0 and 3')

    @patch('builtins.input', side_effect=['10'] * 12)
    def test_full_play(self, input):
        self.assert_stdout('Game Over')
