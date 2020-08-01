"""
Child class of Player class. Implements make_move method. Action will be determined randomly.
"""

from Player import *
import random


class Opponent(Player):

    def make_move(self, pool):
        decision = random.randint(1, 3)

        if decision == 1:
            chosen_card_pool = random.randint(0, 2)
            chosen_card_player = random.randint(0, 2)

            dummy_hand = self.hand[:]
            self.hand[chosen_card_player] = pool.hand[chosen_card_pool]
            pool.hand[chosen_card_pool] = dummy_hand[chosen_card_player]

        elif decision == 3:
            dummy_hand = self.hand[:]
            self.hand = pool.hand[:]
            pool.hand = dummy_hand[:]

        elif decision == 2:
            pass
