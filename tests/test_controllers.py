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
    def test_invalid_first_input_digits(self, input):
        self.assert_stdout('Enter digits between 0 and 10')

    @patch('builtins.input', side_effect=['foo'])
    def test_invalid_first_input_chars(self, input):
        self.assert_stdout('Enter digits between 0 and 10')

    @patch('builtins.input', side_effect=['3', '123'])
    def test_invalid_second_input_digits(self, input):
        self.assert_stdout('Enter digits between 0 and 7')

    @patch('builtins.input', side_effect=['4', 'foo'])
    def test_invalid_second_input_chars(self, input):
        self.assert_stdout('Enter digits between 0 and 6')

    @patch('builtins.input', side_effect=['7', '5'])
    def test_invalid_input_second(self, input):
        self.assert_stdout('Enter digits between 0 and 3')

    @patch('builtins.input', side_effect=[
        '10', '7', '3', '7', '2', '9', '1', '10',
        '10', '10', '2', '3', '6', '4', '7', '1'
    ])
    def test_full_game(self, input):
        self.assert_stdout('Frame 10: 163\n\n\nGame Over')

    @patch('builtins.input', side_effect=[
        '10', '7', '3', '7', '2', '9', '1', '10',
        '10', '10', '2', '3', '6', '4', '7', '3', '3'
    ])
    def test_fill_game(self, input):
        self.assert_stdout('Frame 10: 168\n\n\nGame Over')

    @patch('builtins.input', side_effect=['10'] * 12)
    def test_perfect_game(self, input):
        self.assert_stdout('Frame 10: 300\n\n\nGame Over')
