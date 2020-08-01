"""
Child class of Player class. Implements make_move method to get input from user.
"""

from Player import *


class User(Player):

    def make_move(self, pool):
        print("Choose your Action")
        decision = input("""Enter 1 to exchange 1 card from your hand with the pool,
                                enter 2 to exchange all cards from your hand with the pool
                                enter 3 to skip """)

        while decision != "1" and decision != "2" and decision != "3":
            print("Wrong input. Enter either 1,2 or 3")
            decision = input()

        if decision == "1":
            card_number = {"1": 1, "2": 2, "3": 3}
            card_number_input = input("Enter a number for the card to receive from the pool: ")

            while card_number_input != "1" and card_number_input != "2" and card_number_input != "3":
                print("Wrong input. Enter either 1,2 or 3")
                card_number_input = input()
            chosen_card_pool = card_number[card_number_input]

            card_number_input = input("Enter a number for the card in your hand: ")

            while card_number_input != "1" and card_number_input != "2" and card_number_input != "3":
                print("Wrong input. Enter either 1,2 or 3")
                card_number_input = input()

            chosen_card_user = card_number[card_number_input]

            dummy_hand = self.hand[:]
            self.hand[chosen_card_user - 1] = pool.hand[chosen_card_pool - 1]
            pool.hand[chosen_card_pool - 1] = dummy_hand[chosen_card_user - 1]

        elif decision == "2":
            dummy_hand = self.hand[:]
            self.hand = pool.hand[:]
            pool.hand = dummy_hand[:]

        elif decision == "3":
            pass
