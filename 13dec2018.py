import numpy as np
from enum import IntEnum
import data_13dec2018

map_literal = data_13dec2018.map


class TurnAround(IntEnum):
    left = 0
    straight = 1
    right = 2
    max_turn = 3


class Direction(IntEnum):
    L = 0
    D = 1
    R = 2
    U = 3
    max_dir = 4


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
        self.last_moved = 0

    def moved(self, tick):
        self.last_moved = tick

    def turn_cross(self):
        if self.next_turn == TurnAround.left:
            if self.dir < Direction.max_dir - 1:
                self.dir = self.dir + 1
            else:
                self.dir = 0
        elif self.next_turn == TurnAround.right:
            if not self.dir == 0:
                self.dir = self.dir - 1
            else:
                self.dir = Direction.max_dir - 1
        self.next_turn += 1
        if self.next_turn == TurnAround.max_turn:
            self.next_turn = 0

    def turn_curva(self, curva_char):
        if curva_char == '/':
            if self.dir == Direction.R:     self.dir = Direction.U
            elif self.dir == Direction.D:   self.dir = Direction.L
            elif self.dir == Direction.L:   self.dir = Direction.D
            elif self.dir == Direction.U:   self.dir = Direction.R
        elif curva_char == '\\':
            if self.dir == Direction.R:     self.dir = Direction.D
            elif self.dir == Direction.D:   self.dir = Direction.R
            elif self.dir == Direction.L:   self.dir = Direction.U
            elif self.dir == Direction.U:   self.dir = Direction.L


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

    # Move on
    tick = -1
    while True:
        tick += 1
    #for tick in range(0, max_tick):
        print('tick ' + str(tick))
        for i_r in range(0, map_size[0]):
            for i_c in range(0, map_size[1]):
                if carts[i_r][i_c] is None:
                    continue
                # if it has moved yet
                if carts[i_r][i_c].last_moved >= tick:
                    continue
                # if it is on an intersection, turn
                if map[i_r][i_c] == '+':
                    carts[i_r][i_c].turn_cross()
                # if it is on a turn, turn
                carts[i_r][i_c].turn_curva(map[i_r][i_c])

                direction = carts[i_r][i_c].dir
                # finally, move
                new_r = i_r
                new_c = i_c
                if direction == Direction.L:    new_c -= 1
                elif direction == Direction.R:  new_c += 1
                elif direction == Direction.U:  new_r -= 1
                elif direction == Direction.D:  new_r += 1


                if carts[new_r][new_c] is None:
                    carts[new_r][new_c] = carts[i_r][i_c]
                    carts[i_r][i_c] = None
                    carts[new_r][new_c].moved(tick)
                else:
                    carts[i_r][i_c] = None
                    carts[new_r][new_c] = None
                    map[new_r][new_c] = 'X'
                    # print_position(map, carts)
                    print('crash in ('+ str(new_c) + ', ' + str(new_r) + ')')
                    exit()


        # print_position(map, carts)
