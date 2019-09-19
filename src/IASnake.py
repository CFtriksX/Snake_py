##
## EPITECH PROJECT, 2019
## IASnake.py
## File description:
## IASnake
##

import tensorflow
import random
from variables import *
from Snake import *

def get_block(screen, snake, x, y):
    xiter = int(snake.posx[0] / SNAKE_SIZE)
    yiter = int(snake.posy[0] / SNAKE_SIZE)
    
    while True:
        xiter += x
        yiter += y
        if xiter == screen.candy_pos[0] and yiter == screen.candy_pos[1]:
            return [0, [xiter, yiter]]
        for i in range(0, len(snake.posx)):
            if snake.posx[i] / SNAKE_SIZE == xiter and snake.posy[i] / SNAKE_SIZE == yiter:
                return [2, [xiter, yiter]]
        if xiter < 0 or WIDTH / SNAKE_SIZE <= xiter or yiter < 0 or HEIGHT / SNAKE_SIZE <= yiter:
            return [1, [xiter, yiter]]

def get_far_blocks(screen, snake):
    inpout = []
    inpout.append(get_block(screen, snake, 0, 1))   # D
    inpout.append(get_block(screen, snake, 0, -1))  # U
    inpout.append(get_block(screen, snake, 1, 0))   # R
    inpout.append(get_block(screen, snake, -1, 0))  # L
    inpout.append(get_block(screen, snake, -1, -1)) # UL
    inpout.append(get_block(screen, snake, -1, 1))  # DL
    inpout.append(get_block(screen, snake, 1, -1))  # UR
    inpout.append(get_block(screen, snake, 1, 1))   # DR
    print(inpout)
    return inpout

def get_auth_direction(snake):
    dirs = ['U', 'D', 'L', 'R']
    if (snake.direction == 'L' or snake.direction == 'U'):
        dirs.pop(dirs.index(snake.direction) + 1)
    if (snake.direction == 'R' or snake.direction == 'D'):
        dirs.pop(dirs.index(snake.direction) - 1)
    return dirs

def select_next_direction(screen, snake):
    inpout = get_far_blocks(screen, snake)
    dirs = get_auth_direction(snake)
    return dirs[random.randint(0, 2)]
