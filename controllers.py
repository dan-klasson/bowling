#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Game
import views as view

"""
The controller handles all user input.
It delegates all game logic to the model.
All display content lives in the view.
"""

class GameController:

    def __init__(self):
        self.game = Game()

    def run(self):

        print(view.intro())

        while not self.game.is_over():

            first = self.first_input()
            if not first: continue

            second = self.second_input(first)
            if not second: continue

            self.game.roll(first)
            self.game.roll(second)
            self.print_board()

        print(view.game_over())

    def first_input(self):

        first = input(view.enter_first())

        if not first.isdigit() or int(first) not in range(0, 11):
            print(view.error_invalid_input())
            return False

        first = int(first)

        # skip second roll for strikes and the fill ball
        if first == 10 or len(self.game.results()) == 10:
            self.game.roll(first)
            self.print_board()
            return False

        return first

    def second_input(self, first):

        second = input(view.enter_second())

        if not second.isdigit() or int(second) not in range(0, 11 - first):
            print(view.error_invalid_second(10 - first))
            return False

        return int(second)

    def print_board(self):
        results = self.game.results()
        print(view.score_board(results))
