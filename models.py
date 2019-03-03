#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Game:

    def __init__(self):
        self._frames = [[]]

    @property
    def _current_frame(self):
        return self._frames[-1]

    @property
    def _previous_frames(self):
        """ last 2 frames """
        return self._frames[-3:-1]

    def _assign_bonus(self, score):
        """ assign strike and split bonus """
        for frame in self._previous_frames:
            if len(frame) < 3 and sum(frame) >= 10:
                frame.append(score)

    def _is_frame_played(self):
        """ the frame has been completed by a strike or two rolls """
        return 10 in self._current_frame or len(self._current_frame) > 1

    def is_over(self):
        """
        The game is over when the 10 frames have been completed.
        One extra play is allowed if a strike or split is recorded
        on the tenth frame
        """
        if len(self._frames) >= 10:
            if sum(self._frames[9][:2]) >= 10:
                return len(self._frames[9]) == 3
            else:
                return len(self._frames[9]) == 2
        return False

    def roll(self, score):
        """ each roll of the ball """

        # create new frame if full
        if self._is_frame_played():
            self._frames.append([])

        # record the bonus for splits and strikes
        self._assign_bonus(score)

        # record the roll
        self._current_frame.append(score)

    def results(self):
        """ the result of the current score """
        score, result = 0, []
        for frame in self._frames[:10]:
            score += sum(frame)
            result.append(score)
        return result
