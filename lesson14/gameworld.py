# coding=utf-8

import random
import os
import collections


GRIDSIZE = 10
RANDOMNESS = .9


def draw_grid(cat, mouse):

    """Draws a grid with a cat and a mouse in it"""

    # Clear terminal and set character color to green
    os.system('clear')
    print('\033[92m')
    print('╔' + '══' * GRIDSIZE + '═╗')  # Top border
    for row in range(GRIDSIZE):
        line = '║'
        for col in range(GRIDSIZE):
            if cat.row == row and cat.col == col:
                line += '😺' if is_caught(cat, mouse) else '😼'
            elif mouse.row == row and mouse.col == col:
                line += '🐭'
            else:
                line += '  '
        line += ' ║'
        print(line)
    print('╚' + '══' * GRIDSIZE + '═╝')  # Bottom border


def is_caught(cat, mouse):

    """Determines whether the cat and the mouse are at the same location"""

    return cat.row == mouse.row and cat.col == mouse.col



def move(animal, row=0, col=0):

    """Moves an animal by a specified amount, with some probability of moving
    in another direction
    """

    # Sometimes move in the opposite direction
    if random.random() > RANDOMNESS:
        row = row * -1
        col = row * -1
    # Don't leave the grid!
    new_row = min(GRIDSIZE - 1, max(0, animal.row + row))
    new_col = min(GRIDSIZE - 1, max(0, animal.col + col))
    return Animal(row=new_row, col=new_col)

Animal = collections.namedtuple('Animal', 'row col')
