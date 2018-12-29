import numpy as np
from enum import Enum

import data_15dec2018

class CreatureType(Enum):
    Goblin = 'G'
    Elf = 'E'


class Creature:
    def __init__(self, type):
        self.type = type
        self.next_turn = 0
        self.last_moved = -1
        self.attack_power = 3
        self.hit_points = 200

    def moved(self, tick):
        self.last_moved = tick

    def get_hit(self, points):
        self.hit_points -= points

    def is_alive(self):
        return self.hit_points > 0


def print_path(map):
    for r in range(0, map.shape[0]):
        print(''.join(map[r]))
    print('')


def print_position(map, creatures):
    for r in range(0, map.shape[0]):
        row = map[r].copy()
        for c in range(0, map.shape[1]):
            if creatures[r][c] is not None:
                row[c] = creatures[r][c].type.value

        healt_points = ''
        for c in range(0, map.shape[1]):
            if creatures[r][c] is not None:
                healt_points += ' ' + creatures[r][c].type.value + '(' + str(creatures[r][c].hit_points) + ')'
        print(''.join(row) + healt_points)
    print('')


def init_maps(map_literal):
    size = (len(map_literal), len(max(map_literal, key=len)))
    map = np.ndarray(size, dtype='U1')
    creatures = np.ndarray(size, dtype=object)

    for i_r in range(0, size[0]):
        r = map_literal[i_r]
        for i_c in range(0, size[1]):
            if i_c < len(r): c = r[i_c]
            else: c = ''
            current_position = (i_r, i_c)
            if c == 'E':
                map[current_position] = '.'
                creatures[current_position] = Creature(CreatureType.Elf)
            elif c == 'G':
                map[current_position] = '.'
                creatures[current_position] = Creature(CreatureType.Goblin)
            else:
                map[current_position] = c

    return map, creatures, size


def select_in_range(map, creature, type):
    in_range_map = map.copy()
    for i_r in range(0, map.shape[0]):
        for i_c in range(0, map.shape[1]):
            current_position = (i_r, i_c)
            if creature[current_position] is None:
                continue
            if creature[current_position].type == type:
                continue
            if i_r > 0 and in_range_map[i_r - 1][i_c] == '.':
                in_range_map [i_r - 1][i_c] = '?'
            if i_c > 0 and in_range_map[i_r][i_c - 1] == '.':
                in_range_map[i_r][i_c - 1] = '?'
            if i_r < map.shape[0] and in_range_map[i_r + 1][i_c] == '.':
                in_range_map[i_r + 1][i_c] = '?'
            if i_c < map.shape[1] - 1 and in_range_map[i_r][i_c + 1] == '.':
                in_range_map[i_r][i_c + 1] = '?'
    return in_range_map


def select_distances(map, creatures, start_position):
    distances = -np.ones(map.shape, dtype=np.int32)
    min_dist = 0
    distances[start_position] = min_dist
    added = True
    while added:
        added = False
        for i in range(0, map.shape[0]):
            for j in range(0, map.shape[1]):
                if distances[i][j] == min_dist:
                    if i > 0 and distances[i-1][j] == -1 and map[i-1][j] == '.' and creatures[i-1][j] == None:
                        distances[i-1][j] = min_dist + 1
                        added = True
                    if j > 0 and distances[i][j-1] == -1 and map[i][j-1] == '.' and creatures[i][j-1] == None:
                        distances[i][j-1] = min_dist + 1
                        added = True
                    if i < map.shape[0] - 1 and distances[i+1][j] == -1 and map[i+1][j] == '.' and creatures[i + 1][j] == None:
                        distances[i+1][j] = min_dist + 1
                        added = True
                    if j < map.shape[1] - 1 and distances[i][j+1] == -1 and map[i][j+1] == '.' and creatures[i][j+1] == None:
                        distances[i][j+1] = min_dist + 1
                        added = True
        min_dist += 1
    return distances


def eval_distance(map, creatures, first_point, second_point):
    distances = select_distances(map, creatures, first_point)
    return distances[second_point]


def sort_tuple_list_in_reading_order(tuple_list):
    if len(tuple_list) > 1:
        tuple_list.sort(key=lambda tup: tup[1])
        tuple_list.sort(key=lambda tup: tup[0])
    return tuple_list


def get_adiacent_enemies(map, creatures, current_position, current_type):
    enemies = []

    if current_position[0] > 0:
        new_position = (current_position[0] - 1, current_position[1])
        if creatures[new_position] is not None and creatures[new_position].type != current_type:
            enemies.append(new_position)
    if current_position[1] < map.shape[1] - 1:
        new_position = (current_position[0], current_position[1] + 1)
        if creatures[new_position] is not None and creatures[new_position].type != current_type:
            enemies.append(new_position)
    if current_position[1] > 0:
        new_position = (current_position[0], current_position[1] - 1)
        if creatures[new_position] is not None and creatures[new_position].type != current_type:
            enemies.append(new_position)
    if current_position[0] < map.shape[0] - 1:
        new_position = (current_position[0] + 1, current_position[1])
        if creatures[new_position] is not None and creatures[new_position].type != current_type:
            enemies.append(new_position)


    #enemies = sort_tuple_list_in_reading_order(enemies)
    return enemies


if __name__ == '__main__':
    debug = True

    tests = data_15dec2018.map_tests
    #tests = [data_15dec2018.map_data, -1]
    for test in tests:
        expected_score = test[1]
        map, creatures, map_size = init_maps(test[0])

        game_won = False
        current_round = 0
        last_complete_round = 0

        while not game_won:
            current_round += 1
            if debug:   print('During round ' + str(current_round))

            for i_r in range(0, map_size[0]):
                if game_won: break
                for i_c in range(0, map_size[1]):
                    if game_won: break
                    current_position = (i_r, i_c)
                    if creatures[current_position] is None:
                        continue
                    if creatures[current_position].last_moved >= current_round:
                        continue

                    # Check if it nearby has a different creature type
                    neighbour_position = get_adiacent_enemies(map, creatures, current_position, creatures[current_position].type)

                    # If it has no neighbours, move
                    if len(neighbour_position) == 0:
                        in_range_map = select_in_range(map, creatures, creatures[current_position].type)
                        distances = select_distances(map, creatures, current_position)
                        reachable_point = np.where((in_range_map == '?')*(distances > 0))
                        if len(reachable_point[0]) == 0:
                            continue

                        # Choose direction where to move
                        min_distance = min(distances[reachable_point])
                        chosen_point = np.asarray(np.where((in_range_map == '?') * (distances == min_distance)))
                        chosen_point = chosen_point[:, chosen_point[0] == min(chosen_point[0])]
                        chosen_point = chosen_point[:, chosen_point[1] == min(chosen_point[1])]
                        chosen_point = (chosen_point[0][0], chosen_point[1][0])

                        # Move a step in that direction
                        direction_chosen = False
                        # Try to move Up
                        if (not direction_chosen) and current_position[0] > 0:
                            new_position = (current_position[0] - 1, current_position[1])
                            if distances[new_position] >= 0 and \
                                    eval_distance(map, creatures, new_position, chosen_point) == min_distance - 1:
                                direction_chosen = True
                        # Try to move R
                        if (not direction_chosen) and current_position[1] < map_size[1] - 1:
                            new_position = (current_position[0], current_position[1] + 1)
                            if distances[new_position] >= 0 and \
                                    eval_distance(map, creatures, new_position, chosen_point) == min_distance - 1:
                                direction_chosen = True
                        # Try to move L
                        if (not direction_chosen) and current_position[1] > 0:
                            new_position = (current_position[0], current_position[1] - 1)
                            if distances[new_position] >= 0 and \
                                    eval_distance(map, creatures, new_position, chosen_point) == min_distance - 1:
                                direction_chosen = True
                        # Try to move Down
                        if (not direction_chosen) and current_position[0] < map_size[0] - 1:
                            new_position = (current_position[0] + 1, current_position[1])
                            if distances[new_position] >= 0 and \
                                    eval_distance(map, creatures, new_position, chosen_point) == min_distance - 1:
                                direction_chosen = True

                        if not direction_chosen:
                            print('Error: no direction chosen')
                            exit()

                        if creatures[new_position] is None:
                            creatures[new_position] = creatures[current_position]
                            creatures[current_position] = None
                            creatures[new_position].moved(current_round)
                            current_position = new_position
                        else:
                            print('Error!!!')
                            exit()

                    # If after moving, it reached a enemy, attack
                    neighbour_position = get_adiacent_enemies(map, creatures, current_position, creatures[current_position].type)
                    if len(neighbour_position) > 0:
                        # get weakest neighbour
                        hit_neigh = [creatures[p].hit_points for p in neighbour_position]
                        weak_neigh = neighbour_position[hit_neigh.index(min(hit_neigh))]
                        if debug:
                            print(creatures[current_position].type.value + ' in ' + str(current_position) + ' attack ' +
                                  creatures[weak_neigh].type.value + ' in ' + str(weak_neigh))
                        creatures[weak_neigh].get_hit(creatures[current_position].attack_power)
                        if debug:
                            print(creatures[weak_neigh].type.value + ' in ' + str(weak_neigh) + ' is at ' +
                                  str(creatures[weak_neigh].hit_points) + 'HP')

                        if not creatures[weak_neigh].is_alive():
                            enemy_type = creatures[weak_neigh].type
                            creatures[weak_neigh] = None
                            # check if the game is won from a team
                            if sum([c.type == enemy_type for c in creatures[creatures != None]]) == 0:
                                winner_type = creatures[current_position].type.value
                                score = sum([c.hit_points for c in creatures[creatures != None]])
                                full_score = score*last_complete_round
                                if debug:
                                    print_position(map, creatures)
                                print(winner_type + ' won with a score of ' + \
                                      str(last_complete_round) + ' * ' + str(score) + ' = ' + str(full_score))
                                game_won = True
                                break

            if not game_won:
                last_complete_round = current_round
                if debug or current_round % 100 == 0:
                    print('after round ' + str(current_round))
                    print_position(map, creatures)

        if expected_score > -1:
            if expected_score == full_score:
                print('test ' + str(tests.index(test)) + ' passed! ')
            else:
                print('test ' + str(tests.index(test)) + ' NOT passed! expected score=' + str(expected_score) + ' real score=' + str(full_score))

        exit()