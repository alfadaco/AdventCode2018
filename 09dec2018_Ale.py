import numpy as np
import time


class Marble:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def play_game(n_players, n_marbles):
    # Parameters
    n_multiple = 23
    n_steps = 7
    
    # Initialize list
    marbles = Marble(0)
    marbles.next = marbles
    marbles.prev = marbles

    # Initialize score array
    scores = []
    scores.append(-1)
    for player in range(0,n_players):
        scores.append(0)

    # Execute
    current_marble = marbles
    for m in range(1, n_marbles + 1):
        # Get player number
        current_player = ((m-1) % n_players) + 1

        if m % n_multiple == 0:
            # Go to the seven-th marble prior to the current one
            for i in range(0, n_steps):
                current_marble = current_marble.prev

            # Add score to the current player
            scores[current_player] += m
            scores[current_player] += current_marble.value

            # Remove current marble
            current_marble.prev.next = current_marble.next
            current_marble.next.prev = current_marble.prev

            # Move to the marble following the removed one
            current_marble = current_marble.next
        else:
            # Skip one marble
            current_marble = current_marble.next

            # Add the new marble to the list
            new_marble = Marble(m)
            new_marble.next = current_marble.next
            new_marble.prev = current_marble
            current_marble.next.prev = new_marble
            current_marble.next = new_marble
            current_marble = new_marble

    return marbles, scores


if __name__ == '__main__':
    to_check = [[9, 25], [10, 1618], [13, 7999], [17, 1104], [21, 6111], [30, 5807], [425, 70848], [425, 70848*100]]

    for pair in to_check:
        n_players = pair[0]
        n_marbles = pair[1]
        marbles, scores = play_game(n_players, n_marbles)

        marble = marbles
        array = []
        while True:
            array.append(marble.value)
            marble = marble.next
            if marble.value == 0:
                break

        # Print Scores
        print('Case: ' + str(n_players) + ' players ' + str(n_marbles) + ' marbles')
        winner = scores.index(max(scores))
        print('Winner is player ' + str(winner) + ' with score of ' + str(scores[winner]))
        print('')
