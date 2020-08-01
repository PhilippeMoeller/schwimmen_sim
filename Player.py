"""
Parent class of user, opponents and pool. Sets init method and create_hand method.
"""
import random


class Player:

    def __init__(self, name, card_deck):
        self.life = 3
        self.hand = []
        self.name = name
        self.create_hand(card_deck)

    def create_hand(self, card_deck):
        for i in range(3):
            card = random.randint(0, len(card_deck) - 1)
            self.hand.append(card_deck[card])
            card_deck.remove(card_deck[card])
