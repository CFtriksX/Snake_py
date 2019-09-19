##
## EPITECH PROJECT, 2019
## Snake.py
## File description:
## snake class
##

import random
import pygame
from variables import *

class Snake:
    posx = []
    posy = []
    direction = 'L'
    started = False
    add_last = False

    def __init__(self):
        startx = random.randint(4, int(WIDTH / SNAKE_SIZE) - 5) * SNAKE_SIZE
        starty = random.randint(4, int(HEIGHT / SNAKE_SIZE) - 5) * SNAKE_SIZE
        for i in range(0, 4):
            self.posx.append(startx + i * SNAKE_SIZE)
            self.posy.append(starty)
        print("[start] x", startx, "y", starty)

    def move(self, plusY, plusX):
        last = self.posy[0] + plusY
        temp = 0

        for y in range(0, len(self.posy)):
            temp = self.posy[y]
            self.posy[y] = last
            last = temp
        last = self.posx[0] + plusX
        for x in range(0, len(self.posx)):
            temp = self.posx[x]
            self.posx[x] = last
            last = temp

    def move_snake(self):
        if self.direction == 'U':
            self.move(-SNAKE_SPEED, 0)
        if self.direction == 'D':
            self.move(SNAKE_SPEED, 0)
        if self.direction == 'L':
            self.move(0, -SNAKE_SPEED)
        if self.direction == 'R':
            self.move(0, SNAKE_SPEED)

    def update(self):
        if self.started == False:
            return
        if self.add_last == True:
            to_add = [self.posx[-1], self.posy[-1]]
        self.move_snake()
        if self.add_last == True:
            self.posx.append(to_add[0])
            self.posy.append(to_add[1])
            self.add_last = False

    def draw(self, screen):
        pygame.draw.rect(screen,
                         pygame.Color(0, 255, 0, 255),
                         [self.posx[0], self.posy[0],
                          SNAKE_SIZE, SNAKE_SIZE])
        for i in range(1, len(self.posx)):
                pygame.draw.rect(screen,
                                 pygame.Color(255, 0, 0, 255),
                                 [self.posx[i], self.posy[i],
                                  SNAKE_SIZE, SNAKE_SIZE])
