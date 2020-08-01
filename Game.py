class Game:

    # Determine score of all cards from a players' hand
    def calculate_score(self, player):
        score = {'King': 10, 'Jack': 10, 'Queen': 10, 'Ace': 11}
        points_player = 0

        # Check if a players' hand contains all Aces
        if player[0][1] == "Ace" and player[1][1] == "Ace" and player[2][1] == "Ace":
            print("Player has a Blitz. Everyone loses a life!")
            return

            # If all same suits add 30.5 points
        elif player[0][1] == player[1][1] and player[0][1] == player[2][1]:
            points_player += 30.5

        # Check whether all cards have the same symbol
        elif player[0][0] == player[1][0] and player[0][0] == player[2][0]:
            for numbers in range(len(player)):
                if player[numbers][1] in score:
                    points_player += score[player[numbers][1]]
                else:
                    points_player += int(player[numbers][1])

        # Check whether two cards have the same symbol.
        # If conditions are met check again, whether one of the card is Jack, Queen, King.
        elif player[0][0] == player[1][0]:
            if player[0][1] in score and player[1][1] in score:
                points_player += score[player[0][1]] + score[player[1][1]]
            elif player[1][1] in score:
                points_player += score[player[1][1]] + int(player[0][1])
            elif player[0][1] in score:
                points_player += score[player[0][1]] + int(player[1][1])
            else:
                points_player += int(player[0][1]) + int(player[1][1])

        elif player[1][0] == player[2][0]:
            if player[1][1] in score and player[2][1] in score:
                points_player += score[player[1][1]] + score[player[2][1]]
            elif player[1][1] in score:
                points_player += score[player[1][1]] + int(player[2][1])
            elif player[2][1] in score:
                points_player += score[player[2][1]] + int(player[1][1])
            else:
                points_player += int(player[2][1]) + int(player[1][1])

        elif player[0][0] == player[2][0]:
            if player[0][1] in score and player[2][1] in score:
                points_player += score[player[0][1]] + score[player[2][1]]
            elif player[0][1] in score:
                points_player += score[player[0][1]] + int(player[2][1])
            elif player[2][1] in score:
                points_player += score[player[2][1]] + int(player[0][1])
            else:
                points_player += int(player[0][1]) + int(player[2][1])

        else:
            for numbers in range(len(player)):
                appender = []
                if player[numbers][1] in score:
                    appender.append(score[player[numbers][1]])
                else:
                    appender.append(int(player[numbers][1]))

            points_player += max(appender)

        return points_player
