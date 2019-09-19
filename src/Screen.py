###
## EPITECH PROJECT, 2019
## Screen.py
## File description:
## screen class
##

import pygame
from Snake import *
from variables import *
from IASnake import *

class Screen:
    running = True
    candy_pos = [0, 0]
    map = []
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        for x in range(0, int(WIDTH / SNAKE_SIZE)):
            self.map.append([])
            for y in range(0, int(HEIGHT / SNAKE_SIZE)):
                self.map[x].append(int(0))

    def event_ticks(self, snake):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_UP and snake.direction != 'D':
#                    snake.direction = 'U'
#                    snake.started = True
#                if event.key == pygame.K_DOWN and snake.direction != 'U':
#                    snake.direction = 'D'
#                    snake.started = True
#                if event.key == pygame.K_LEFT and snake.direction != 'R':
#                    snake.direction = 'L'
#                    snake.started = True
#                if event.key == pygame.K_RIGHT and snake.direction != 'L':
#                    snake.direction = 'R'
#                    snake.started = True

    def verify_candy(self, snake):
        xpos = int(snake.posx[0] / SNAKE_SIZE)
        ypos = int(snake.posy[0] / SNAKE_SIZE)
        if self.map[xpos][ypos] == 1:
            snake.add_last = True
            self.map[xpos][ypos] = 0
        ok_one = False
        for area in self.map:
            if 1 in area:
                ok_one = True
        if ok_one == False:
            xpos = random.randint(0, int(WIDTH / SNAKE_SIZE) - 1)
            ypos = random.randint(0, int(HEIGHT / SNAKE_SIZE) - 1)
            self.candy_pos = [xpos, ypos]
            self.map[xpos][ypos] = 1

    def verify_end(self, snake):
        for i in range(0, len(snake.posx)):
            for j in range(0, len(snake.posy)):
                if snake.posx[i] == snake.posx[j] and snake.posy[i] == snake.posy[j] and i != j:
                    self.running = False        
        posx = snake.posx[0] / SNAKE_SIZE
        posy = snake.posy[0] / SNAKE_SIZE
        if posx < 0 or posy < 0 or int(WIDTH / SNAKE_SIZE) <= posx or int(HEIGHT / SNAKE_SIZE) <= posy:
            self.running = False

    def update(self, snake, nextdir):
        self.event_ticks(snake)
        snake.direction = nextdir
        snake.started = True
        self.verify_candy(snake)
        snake.update()
        self.verify_end(snake)

    def draw(self, snake):
        self.screen.fill(pygame.Color(0, 0, 0, 255))
        pygame.draw.rect(self.screen,
                         pygame.Color(255, 255, 255, 255),
                         [self.candy_pos[0] * SNAKE_SIZE,
                          self.candy_pos[1] * SNAKE_SIZE,
                          SNAKE_SIZE, SNAKE_SIZE])
        snake.draw(self.screen)
        pygame.display.flip()
