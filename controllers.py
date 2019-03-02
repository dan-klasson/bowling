#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Game
from views import *

class GameController:

    def __init__(self):
        self.game = Game()

    def run(self):

        print(intro())

        while not self.game.is_over():

            first = input(enter_first())

            if first == '10':
                self.game.roll(int(first))
                results = self.game.results()
                print(score_board(results))
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

            self.game.roll(first)
            self.game.roll(second)

            results = self.game.results()
            print(score_board(results))

        print(game_over())


         