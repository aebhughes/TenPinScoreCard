#!/usr/bin/env python

"""
Class for a ten-pin bowling scoring application, or even a ten-pin
bowling simulation / game.

Once instituted, the resulting object maintains a score-card of
ten frames of a ten-pin bowling game. Usage:

   player1 = bowler.BowlScore()
   player2 = bowler.BowlScore() # one object per player

per turn:

    player.Go(<pins_down_ball1>, <pins_down_ball2>)

Results:

    player.ScoreCard  # scorecard as a tuple of lists, one list per frame
                      # where the current score is None, a Strike or Spare
                      # has been detected.  The running score can only be
                      # determined from the play of the next frame.

    player.FrameNo    # Current frame being played
    player.Message    # Any error / information messages.

Only 10 frames can be played.  Any attempts to play more than that will
simply return last successful play. More than 10 pins in play is simply
ignored except for a message in player.Message, as are any other errors.

TODO:  This class is being developed using TDD. See attached tests/unittest
       module.

"""

class BowlScore(object):

    def __init__(self):
        self.ScoreCard = []
        self.FrameNo = 1
        self.Message = 'Begin play!'


    def ScoreCard(self):
        pass


    def Go(self, ball1, ball2):
        score = 0
        for parm in [ball1, 
        if ball1 + ball2 > 10:
            self.Message = 'INVALID: %d pins recorded' % (ball1 + ball2)
            return
