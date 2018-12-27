import numpy as np
import time


def brute_force(n_players, last_marble, marble_to_be_removed, n_multiple):
    marble_played = []
    players_score = np.zeros(n_players, dtype=np.uint)
    current_player = -1
    current_marble = 0

    last_range = time.time()

    for m in range(0, last_marble + 1):
        if m > 0 and m % n_multiple == 0:
            current_marble -= 2 + marble_to_be_removed
            if current_marble < 0:
                current_marble += len(marble_played)
            players_score[current_player] += m
            players_score[current_player] += marble_played.pop(current_marble)
        else:
            marble_played.insert(current_marble, m)

        if m % 100000 == 0:
            new_time = time.time()
            print(str(int(m/1000)) + 'k / ' + str(int((last_marble+1)/1000)) + 'k dt=' + str(round(new_time - last_range)) + 's')
            last_range = new_time

        current_marble += 2
        current_player += 1

        if current_player >= n_players:
            current_player = 0
        if current_marble > len(marble_played):
            current_marble = 1

    return marble_played, players_score


if __name__ == '__main__':
    to_check = [[9, 25], [10, 28000], [10, 1618], [13, 7999], [17, 1104], [21, 6111], [30, 5807], [425, 70848], [425, 70848*100]]

    # Removing logic
    marble_to_be_removed = 7
    n_multiple = 23

    for pair in to_check:
        n_players = pair[0]
        last_marble = pair[1]

        # Insert marbles
        marble_played, players_score = brute_force(n_players, last_marble, marble_to_be_removed, n_multiple)

        # Print Scores
        print('Case: ' + str(n_players) + ' players ' + str(last_marble) + ' marbles')
        winner = players_score.argmax()
        print('Winner is player ' + str(winner) + ' with score of ' + str(players_score[winner]))
        #winner = players_score2.argmax()
        #print('Winner is player ' + str(winner) + ' with score of ' + str(players_score2[winner]))
        print('')
