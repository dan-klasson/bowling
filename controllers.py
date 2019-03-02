#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Game
from views import *

"""
The controller here handles all user input.
It delegates all game logic to the model. 
All display logic lives in the view.
"""

class GameController:

    def __init__(self):
        self.game = Game()

    def handle_strike(self, first):
        self.game.roll(int(first))
        results = self.game.results()
        print(score_board(results))

    def handle_rolls(self, first, second):
        self.game.roll(first)
        self.game.roll(second)

        results = self.game.results()
        print(score_board(results))

    def run(self):

        print(intro())

        while not self.game.is_over():

            first = input(enter_first())

            if first == '10':
                self.handle_strike(first)
                continue

            if not first.isdigit() or int(first) not in range(0, 11):
                print(error_invalid_input())
                continue

            second = input(enter_second())

            if not second.isdigit():
                print(error_invalid_input())
                continue

            first, second = int(first), int(second)

            if second not in range(0, 11 - first):
                print(error_invalid_second(10 - first))
                continue

            self.handle_rolls(first, second)

        print(game_over())

         