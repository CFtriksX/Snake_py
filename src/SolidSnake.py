#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## SolidSnake.py
## File description:
## solidsnake
##

import pygame
import sys
import time
from Screen import *
from Snake import *
from variables import *

def create_screen():
    screen = Screen()
    snake = Snake()
    
    while (screen.running):
        screen.update(snake, select_next_direction(screen, snake))
        screen.draw(snake)
        time.sleep(SNAKE_SLEEP)

def main():
    create_screen()

if __name__ == '__main__':
    main()
