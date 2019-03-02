#!/usr/bin/env python
# -*- coding: utf-8 -*-

def intro():
    return '\nBowling Score:\n'

def score_board(scores):
    output = "\nYour Score:"
    for index, score in enumerate(scores):
        output += "\nFrame {}: {}".format(index + 1, score)
    output += "\n"
    return output

def enter_first():
    return "Enter 1st roll: "

def enter_second():
    return "Enter 2nd roll: "

def game_over():
    return "\nGame Over\n"

def error_invalid_input():
    return "\nInvalid input. Enter digits between 0 and 10\n"

def error_invalid_second(value):
    return "\nInvalid input. Enter digits between 0 and {}\n".format(value)
