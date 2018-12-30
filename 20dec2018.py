from enum import Enum
from matplotlib import pyplot as plt
import numpy as np
import data_20dec2018

class CellType(Enum):
    Start = 'X'
    Wall = '#',
    Room = ',',
    DoorH = '-',
    DoorV = '|',
    Unknown = '?'


def fill_position(map, pos, new_char):
    if pos[0] == 0 or pos[1] == 0 or pos[0] >= map.shape[0] or pos[1] >= map.shape[1]:
        print('Error! to small map given')
        exit()

    # Fill center position
    map[pos] = new_char

    # Fill corners
    for dx in [-1, 1]:
        for dy in [-1, 1]:
            if map[pos[0] - dx, pos[1] - dy] is None:
                map[pos[0] - dx, pos[1] - dy] = CellType.Wall

    # Fill other parts
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if map[pos[0] - dx, pos[1] - dy] is None:
                map[pos[0] - dx, pos[1] - dy] = CellType.Unknown


def draw_map(map):
    drawn_map = np.ndarray(map.shape, dtype=np.uint8)
    drawn_map[map == None] = 180
    drawn_map[map == CellType.Start] = 0
    drawn_map[map == CellType.Wall] = 50
    drawn_map[map == CellType.Room] = 220
    drawn_map[map == CellType.DoorH] = 240
    drawn_map[map == CellType.DoorV] = 240
    drawn_map[map == CellType.Unknown] = 180
    plt.imshow(drawn_map, cmap='hsv', vmin=0, vmax=255)
    plt.draw()
    plt.pause(0.01)
    plt.show(block=False)

def tuple_min(tuple1, tuple2):
    return (min(tuple1[0], tuple2[0]), min(tuple1[1], tuple2[1]))

def tuple_max(tuple1, tuple2):
    return (max(tuple1[0], tuple2[0]), max(tuple1[1], tuple2[1]))

def go_on_until_group_end(regex):
    counter = 0
    while len(regex) > 0:
        if regex[0] == '(':
            counter += 1
        elif regex[0] == ')':
            counter -= 1
            if counter < 0:
                return regex
        regex = regex[1:]
    return regex


def get_next_subgroup(regex):
    counter = 0
    while len(regex) > 0:
        if regex[0] == '|' and counter == 0:
            return regex
        elif regex[0] == '(':
            counter += 1
        elif regex[0] == ')':
            counter -= 1
            if counter < 0:
                return regex
        regex = regex[1:]
    return regex


def eval_min_max(regex, current_coord, info_counter, min_coord=(0,0), max_coord=(0,0)):
    exit_chars = ['$']
    while regex[0] not in exit_chars:
        info_counter += 1
        if info_counter % 10000 == 0:
            print(str(min_coord), str(max_coord))
            info_counter = 0

        dr = 0
        dc = 0
        if regex[0] == 'E':     dc = 1
        elif regex[0] == 'W':   dc = -1
        elif regex[0] == 'N':   dr = -1
        elif regex[0] == 'S':   dr = 1
        elif regex[0] == ')':   pass
        elif regex[0] == '|':   # I have to skip until first alone )
            regex = go_on_until_group_end(regex[1:])
        elif regex[0] == '(':
            # Start new regex
            new_min_coord, new_max_coord, info_counter = eval_min_max(regex[1:], current_coord, info_counter, min_coord, max_coord)
            min_coord = tuple_min(min_coord, new_min_coord)
            max_coord = tuple_max(max_coord, new_max_coord)

            # Find all | of current group
            regex = get_next_subgroup(regex[1:])
            while len(regex) > 0 and regex[0] != ')':
                new_min_coord, new_max_coord, info_counter = eval_min_max(regex[1:], current_coord, info_counter, min_coord, max_coord)
                min_coord = tuple_min(min_coord, new_min_coord)
                max_coord = tuple_max(max_coord, new_max_coord)
                regex = get_next_subgroup(regex[1:])

            return min_coord, max_coord, info_counter

        current_coord = (current_coord[0] + dr, current_coord[1] + dc)
        min_coord = tuple_min(min_coord, current_coord)
        max_coord = tuple_max(max_coord, current_coord)
        regex = regex[1:]

    return min_coord, max_coord, info_counter


def create_map(regex, current_coord, map, info_counter):
    exit_chars = ['$']
    moving_chars = ['E', 'S', 'N', 'W']
    while regex[0] not in exit_chars:
        if regex[0] in moving_chars:
            info_counter += 1
            if info_counter % 1000 == 0:
                draw_map(plant)
                info_counter = 0
            dr = 0
            dc = 0
            if regex[0] == 'E':
                dc = 1
                door_type = CellType.DoorV
            elif regex[0] == 'W':
                dc = -1
                door_type = CellType.DoorV
            elif regex[0] == 'N':
                dr = -1
                door_type = CellType.DoorH
            elif regex[0] == 'S':
                dr = 1
                door_type = CellType.DoorH
            map[(current_coord[0] + dr, current_coord[1] + dc)] = door_type
            current_coord = (current_coord[0] + 2*dr, current_coord[1] + 2*dc)
            fill_position(map, current_coord, CellType.Room)
        elif regex[0] == ')': pass
        elif regex[0] == '|':   # I have to skip until first alone )
            regex = go_on_until_group_end(regex[1:])
        elif regex[0] == '(':
            group_count = 0

            # Start new regex
            create_map(regex[1:], current_coord, map, info_counter)

            # Find all | of current group
            group_count += 1
            regex = get_next_subgroup(regex[1:])
            while len(regex) > 0 and regex[0] != ')':
                create_map(regex[1:], current_coord, map, info_counter)
                regex = get_next_subgroup(regex[1:])
                group_count += 1
            return info_counter
        regex = regex[1:]
    return info_counter


if __name__ == '__main__':
    test_regexs = data_20dec2018.real_data

    for test in test_regexs:
        regex = test['data']
        max_dist = test['max_distance']
        info_counter = 0

        # Get plant size
        current_coord = (0, 0)
        min_coord, max_coord = eval_min_max(regex[1:], current_coord, info_counter)
        plant_shape = ((max_coord[0] - min_coord[0] + 1) * 2 + 1, (max_coord[1] - min_coord[1] + 1) * 2 + 1)
        start_position = ((current_coord[0] - min_coord[0]) * 2 + 1, (current_coord[1] - min_coord[1]) * 2 + 1)
        print('Plant size = ' + str(plant_shape))

        # Creating plant
        plt.figure()
        plant = np.ndarray(plant_shape, dtype=object)
        if regex[0] == '^':
            fill_position(plant, start_position, CellType.Start)
            draw_map(plant)
            plt.colorbar()
        create_map(regex[1:], start_position, plant, info_counter)
        plant[plant == CellType.Unknown] = CellType.Wall
        draw_map(plant)

        # Creating plant distances
        distances = -np.ones(plant_shape, dtype=int)
        changed = True
        last_distance = 0
        distances[start_position] = last_distance
        while changed:
            changed = False
            for i_r in range(0, plant_shape[0]):
                for i_c in range(0, plant_shape[1]):
                    if distances[i_r, i_c] == last_distance:
                        ds = [(-1, 0), (0, -1), (1, 0), (0, 1)]
                        for s in ds:
                            new_coors = (i_r + s[0], i_c + s[1])
                            if new_coors[0] > 0 and new_coors[1] > 0 and new_coors[0] < plant_shape[0] and new_coors[1] < plant_shape[1]:
                                if distances[new_coors] == -1 and plant[new_coors] != CellType.Wall:
                                    distances[new_coors] = last_distance + 1
                                    changed = True
            last_distance += 1

        plt.figure()
        plt.imshow(distances)

        # Get max distance
        print('Furthest room is ' + str(distances.max()) + ' cells from the starting one')
        print('Reaching the furthest room means to pass through ' + str(distances.max()/2) + ' ports')

        if distances.max()/2 != max_dist:
            print('Test error ' + regex)
            a = 1
        print('')

    plt.show()
