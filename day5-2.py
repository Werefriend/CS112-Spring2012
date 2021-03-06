#!/usr/bin/env python

import pygame
from pygame.locals import *
# Settings
BLACK = 0,0,0
RED = 255,0,0
size = 400,400

#initialize stuff
pygame.init()
screen = pygame.display.set_mode(size)
sep = 8

pygame.key.set_repeat(100,100)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == KEYDOWN and event.key == K_UP:
            sep += 1
        elif event.type == KEYDOWN and event.key == K_DOWN:
            sep -= 1


    ## DRAW
    screen.fill(BLACK)
    for i in range(0,400,sep):
        pygame.draw.line(screen,RED,(0,i),(i,399))
        pygame.draw.line(screen,RED,(i,399),(399,399-i))
        pygame.draw.line(screen,RED,(399,399-i),(399-i,0))
        pygame.draw.line(screen,RED,(399-i,0),(0,i))

    pygame.display.flip()

#(1) CHECK Curve in all corners
#(2) CHECK Use variable steps for key downs
#(3) Holding  a key down

#HINT investigate set_repeat


