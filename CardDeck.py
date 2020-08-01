"""
This class creates the card deck out of all suits and numbers available in a Schwimmen game.
"""


class CardDeck:
    suits = ["Spade", "Heart", "Diamond", "Club"]
    numbers = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    card_deck = []

    def merge_suits_numbers(self):
        for suit in self.suits:
            for number in self.numbers:
                self.card_deck.append((suit, number))

        return self.card_deck
