"""
Schwimmen - Card Game
The main class creates all objects to start the game.
The game will be executed in a while loop which will be
terminated when the user's life has reached 0 or when both
of the opponents's life have reached 0.
"""
from CardDeck import CardDeck
from User import User
from Opponent import Opponent
from Pool import Pool
from Game import Game

# Create a card deck, user, 2 x opponent, a pool and a game object
carddeck = CardDeck()
# Merges Suits and Numbers
carddeck.merge_suits_numbers()

# Initialize objects by giving them names and card deck lists
user = User("User", carddeck.card_deck)
opponent = Opponent("Opponent", carddeck.card_deck)
opponent2 = Opponent("Opponent2", carddeck.card_deck)
pool = Pool("Pool", carddeck.card_deck)
game = Game()

# The game will be executed as long as the user's life has not reached 0
while user.life > 0:

    # Display life points, cards in the pool and user cards
    print("-" * 75, "\n")
    print("User Life: {user_life} | Opponent Life: {opponent_life} | Opponent2 Life: {opponent2_life}\n".format(
        user_life=user.life, opponent_life=opponent.life, opponent2_life=opponent2.life))
    print("-" * 75, "\n")
    print("My cards: {user_hand}\nPool: {pool_cards}\n".format(user_hand=user.hand, pool_cards=pool.hand))
    print("-" * 75, "\n")

    #  Check whether all opponents' life have reached 0, if yes,
    if not opponent.life > 0 and opponent2.life > 0:
        print("You win!")
        break

    point_list = []

    # Each participating player makes a move. Pass the pool object to from which each player may exchange cards from.
    user.make_move(pool)
    user_points = game.calculate_score(user.hand)

    # Opponents may only exchange card if their lives are higher than 0. If not they will be excluded from score
    # calculation by assigning 32 to the opponent_points attribute.
    if opponent.life > 0:
        opponent.make_move(pool)
        opponent_points = game.calculate_score(opponent.hand)
    else:
        print("Opponent lost")
        opponent_points = 32

    if opponent2.life > 0:
        opponent2.make_move(pool)
        opponent2_points = game.calculate_score(opponent2.hand)
    else:
        print("Opponent2 lost")
        opponent2_points = 32

    # Create dict. with player objects as keys and points as values to determine player and their score
    points_dict = {user: user_points, opponent: opponent_points, opponent2: opponent2_points}

    min_value = min(points_dict.values())

    # If player score is equal to min value subtract 1 from their life attribute
    if not list(filter(lambda x: x != min_value, points_dict.values())):
        print("Draw!")
    else:
        for key, value in points_dict.items():
            if value == min_value:
                key.life -= 1
                print(key.name, "lost a life")

    print("Min Value ", min_value)
    print("My points", user_points)
    print("Opponent points", opponent_points)
    print("Opponent2 points", opponent2_points)

print("Game Over.")
