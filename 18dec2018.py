from enum import Enum
import numpy as np
import matplotlib.pyplot as plt
import time

import data_18dec2018


class AcreType(Enum):
    Ground = '.'
    Tree = '|'
    Lumberyard = '#'


def init_area(literal_area):
    # eval shape
    area_shape = (len(literal_area), len(max(literal_area, key=len)))
    # create nd array
    area_array = np.ndarray(area_shape, dtype=object)

    # fill arrays
    for i_r in range(0, area_shape[0]):
        for i_c in range(0, area_shape[1]):
            element = literal_area[i_r][i_c]
            area_array[i_r][i_c] = AcreType(element)
    return area_array


def count_neighbour(map, pos, type):
    min_x = max(0, pos[0] - 1)
    max_x = min(map.shape[0], pos[0] + 2)
    min_y = max(0, pos[1] - 1)
    max_y = min(map.shape[1], pos[1] + 2)
    sub_map = map[min_x:max_x, min_y:max_y]
    counted = sum(sum(sub_map == type)) - (map[pos] == type)
    return counted


def change_acre_status(map, pos):
    new_type = map[pos]

    if new_type == AcreType.Ground:
        if count_neighbour(map, pos, AcreType.Tree) >= 3:
            new_type = AcreType.Tree
    elif new_type == AcreType.Tree:
        if count_neighbour(map, pos, AcreType.Lumberyard) >= 3:
            new_type = AcreType.Lumberyard
    elif new_type == AcreType.Lumberyard:
        if count_neighbour(map, pos, AcreType.Lumberyard) == 0 or \
                count_neighbour(map, pos, AcreType.Tree) == 0:
            new_type = AcreType.Ground
    return new_type


def print_map(map):
    for i_r in range(0, area_array.shape[0]):
        map_string = ''
        for i_c in range(0, area_array.shape[1]):
            map_string += map[i_r, i_c].value
        print(map_string)
    print()


if __name__ == '__main__':
    area_array = init_area(data_18dec2018.data_input)
    area_img = np.ndarray(area_array.shape, dtype=np.uint8)
    print('Start ')

    area_img[area_array == AcreType.Ground] = 0
    area_img[area_array == AcreType.Tree] = 1
    area_img[area_array == AcreType.Lumberyard] = 2
    plt.imshow(area_img)
    plt.title('Start')
    plt.colorbar()
    plt.draw()
    plt.pause(0.01)
    plt.show(block=False)

    for tick in range(1, 1000000000 + 1):
        start = time.time()
        new_area = area_array.copy()
        for i_r in range(0, area_array.shape[0]):
            for i_c in range(0, area_array.shape[1]):
                position = (i_r, i_c)
                new_area[position] = change_acre_status(area_array, position)

        area_array = new_area

        count_wood = sum(sum(area_array == AcreType.Tree))
        count_lumberyard = sum(sum(area_array == AcreType.Lumberyard))

        if tick % 10 == 0:
            stop = time.time()
            print('After ' + str(tick) + ' minutes')
            print('Elapsed time ' + str(stop - start) + ' s')
            area_img[area_array == AcreType.Ground] = 0
            area_img[area_array == AcreType.Tree] = 1
            area_img[area_array == AcreType.Lumberyard] = 2
            plt.imshow(area_img)
            plt.title('Area after ' + str(tick) + ' minutes')
            plt.draw()
            plt.pause(0.01)
            plt.show(block=False)
            last_score = count_wood * count_lumberyard
            print('Resource value = ' + str(count_wood) + ' * ' + str(count_lumberyard) + ' = ' + str(last_score))


    plt.show()