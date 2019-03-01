#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Game:

    def __init__(self):
        self._frames = [[]]
        self._game_over = False

    @property
    def _current_frame(self):
        return self._frames[-1]

    @property
    def _previous_frames(self):
        return self._frames[-3:-1]

    def _is_frame_played(self):
        return 10 in self._current_frame or len(self._current_frame) > 1

    def _assign_frame_bonus(self, score):
        for frame in self._previous_frames:
            if len(frame) < 3 and sum(frame) >= 10:
                frame.append(score)
    
    def is_over(self):
        if len(self._frames) >= 10:
            if sum(self._frames[9][:2]) >= 10:
                return len(self._frames[9]) == 3
            else:
                return len(self._frames[9]) == 2
        return False

    def roll(self, score):

        if self._is_frame_played():
            self._frames.append([])
            
        self._assign_frame_bonus(score)
        self._current_frame.append(score)

    def results(self):
        score, result = 0, []
        for frame in self._frames[:10]:
            score += sum(frame)
            result.append(score)
        return result
