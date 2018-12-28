import numpy as np
from enum import Enum
import data_13dec2018

map_literal = data_13dec2018.map_test


class TurnAround(Enum):
    left = 0
    straight = 1
    right = 2


class Direction(Enum):
    L = 0
    R = 1
    U = 2
    D = 3


def convert_dir_to_char(dir):
    if dir == Direction.L:
        return '<'
    elif dir == Direction.R:
        return '>'
    elif dir == Direction.U:
        return '^'
    elif dir == Direction.D:
        return 'v'
    return 'o'


class Cart:
    def __init__(self, dir):
        self.dir = dir
        self.next_turn = 0


def print_path(map):
    for r in range(0, map.shape[0]):
        print(''.join(map[r]))


def print_position(map, carts):
    for r in range(0, map.shape[0]):
        row = map[r].copy()
        for c in range(0, map.shape[1]):
            if carts[r][c] is not None:
                row[c] = convert_dir_to_char(carts[r][c].dir)
        print(''.join(row))


if __name__ == '__main__':
    map_size = (len(map_literal), len(max(map_literal, key=len)))
    map = np.ndarray(map_size, dtype='U1')
    carts = np.ndarray(map_size, dtype=object)

    vCart = np.vectorize(Cart)

    for i_r in range(0, len(map_literal)):
        r = map_literal[i_r]
        for i_c in range(0, map_size[1]):
            if i_c < len(r):
                c = r[i_c]
            else:
                c = ''
            if c == '<':
                map[i_r][i_c] = '-'
                carts[i_r][i_c] = Cart(Direction.L)
            elif c == '>':
                map[i_r][i_c] = '-'
                carts[i_r][i_c] = Cart(Direction.R)
            elif c == '^':
                map[i_r][i_c] = '|'
                carts[i_r][i_c] = Cart(Direction.U)
            elif c == 'v':
                map[i_r][i_c] = '|'
                carts[i_r][i_c] = Cart(Direction.D)
            else:
                map[i_r][i_c] = c

    print_path(map)
    print_position(map, carts)
