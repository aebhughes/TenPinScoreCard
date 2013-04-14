import unittest
import bowler     # class that manages game play scores for 10-pin
                  # instantiate for each player

"""
Bowling Scoring 
===============
The game of 10 pin bowling consists of 10 frames. In each frame the player 
has two opportunities to knock down 10 pins.  The score for the frame is 
the total number of pins knocked down, plus bonuses for strikes and spares.

A 'spare' is when the player knocks down all 10 pins in two tries.  The 
bonus for that frame is the number of pins knocked down by the next roll.  

A strike is when the player knocks down all 10 pins on his first try.  
The bonus for that frame is the value of the next two balls rolled.

In the tenth frame a player who rolls a spare or strike is allowed to 
roll the extra balls to complete the frame.  However no more than three 
balls can be rolled in tenth frame.
"""

class Expected(unittest.TestCase):
    # ------------------------------------------------------------- 
    # tuple def: (First Ball, Second Ball, running score)
    # .. a running score of None indicates a Strike or Spare
    # ------------------------------------------------------------- 
    KnownValues = ( ([1, 4,  5]),                                 # 1)
                    ([1, 4,  5],   [4, 5, 14]),                   # 2)
                    ([1, 4,  5],   [4, 5, 14],    [6, 4, None]),  # 3)
                    ([1, 4,  5],   [4, 5, 14],    [6, 4, 29],
                     [6, 4, None]),                               # 4)
                    ([1, 4,  5],   [ 4, 5, 14],   [6, 4, 29],
                     [6, 4, 49],   [10, 0, None]),                # 5)
                    ([1, 4,  5],   [4, 5, 14],    [6, 4, 29],
                     [6, 4, 49],   [10, 0, 60],   [0, 1, 61]),    # 6)
                    ([1, 4,  5],   [4, 5, 14],    [6, 4, 29],
                     [6, 4, 49],   [10, 0, 60],   [0, 1, 61],
                     [7, 3, None]),                               # 7)
                    ([1, 4,  5],   [4, 5, 14],    [6, 4, 29],
                     [6, 4, 49],   [10, 0, 60],   [0, 1, 61],
                     [7, 3, 77],   [6, 4, None]),                 # 8)
                    ([1, 4,  5],   [4, 5, 14],    [6, 4, 29],
                     [6, 4, 49],   [10, 0, 60],   [0, 1, 61],
                     [7, 3, 77],   [6, 4, 97],    [10, 0, None]), # 9)
                    ([1, 4,  5],   [4, 5, 14],    [6, 4, 29],
                     [6, 4, 49],   [10, 0, 60],   [0, 1, 61],
                     [7, 3, 77],   [6, 4, 97],    [10, 0, 117],
                     [2, 8, None]),                               # 10)
                    ([1, 4,   5],  [ 4, 5, 14],   [ 6, 4,  29],
                     [6, 4,  49],  [10, 0, 60],   [ 0, 1,  61],
                     [7, 3,  77],  [ 6, 4, 97],   [10, 0, 117],
                     [6, None, 133])                                 # Extra
                   )

    def testKnown(self):
        player = bowler.BowlScore()
        frame_no = 1
        for card in self.KnownValues:
            if type(card) == list:
                ball1, ball2, score = card
            else:
                ball1, ball2, score = card[-1]
            player.Go(ball1, ball2)
            self.assertEqual(player.ScoreCard, card)
            if frame_no < 11:
                self.assertEqual(player.FrameNo, frame_no)
            frame_no += 1
        self.assertEqual(player.Message, 'Game over')  # normal end

    def testTooMany(self):
        player = bowler.BowlScore()
        for card in self.KnownValues:
            if type(card) == list:
                ball1, ball2, score = card
            else:
                ball1, ball2, score = card[-1]
            player.Go(ball1, ball2)
        self.assertEqual(player.Message, 'Game over')
        self.assertEqual(player.FrameNo, 10)
        # Play one frame extra
        player.Go(1,2)
        # should not effect scorecard
        self.assertEqual(player.Message, 'Game over')  # too many = normal end
        self.assertEqual(player.FrameNo, 10)


    def testInvalidInput(self):
        player = bowler.BowlScore()
        self.assertIsNone(player.Go(5,6))
        self.assertEqual(player.Message, 'INVALID: 11 pins recorded')
        self.assertEqual(player.FrameNo, 1)
        self.assertIsNone(player.Go(15,6))
        self.assertEqual(player.Message, 'INVALID: 21 pins recorded')
        self.assertEqual(player.FrameNo, 1)


    def testBasics(self):
        player = bowler.BowlScore()
        self.assertEqual(player.FrameNo, 1)
        self.assertEqual(player.ScoreCard, [])
        self.assertEqual(player.Message, 'Begin play!')

if __name__ == '__main__':
    unittest.main()
