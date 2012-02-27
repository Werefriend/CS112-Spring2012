#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""


import pygame
from pygame import draw
from pygame.locals import *
from random import *

#inititalize some stuff I'll need
playing = False
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
screen.fill((0,0,0))
done = False
screen_bounds = screen.get_rect()
winner = 0
p1x, p1y = 80, 300
p1dx, p1dy = 0, 0
p2x, p2y = 720, 300
p2dx, p2dy = 0, 0
p1trail = []
p2trail = []
cross = []

BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)

def drawSquares(surf, pos, color =(255,255,255), square=10):
    x,y = pos
    draw.rect(surf, color, (x, y, square, square))

#allows each player to move according to given buttons and boundaries
def move(x, y, dx, dy, up, down, left, right, bounds):
    x += dx
    y += dy
    
    if event.type == KEYDOWN and event.key == up and dy != 10:
        dx = 0
        dy = -10
    if event.type == KEYDOWN and event.key == down and dy != -10:
        dx = 0
        dy = 10
    if event.type == KEYDOWN and event.key == left and dx != 10:
        dx = -10
        dy = 0
    if event.type == KEYDOWN and event.key == right and dx != -10:
        dx = 10
        dy = 0
    if y < bounds.top or y > bounds.bottom:
        dx, dy = 0, 0
        playing = False
    if x < bounds.left or x > bounds.right:
        dx, dy = 0,0
        playing = False
    return x, y, dx, dy


#freeze the screen, indicate a winner, restart with space
#def finito():

#mo'fuggin' GAME LOOP BYATCH
while not done:
    #quitting that shit
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
    #starting the game (you just lost the game)
    if event.type == KEYDOWN and event.key == K_SPACE and p1x == 80 and  p1y == 300 and p2x == 720 and p2y == 300:
        p1dx, p1dy = 10, 0
        p2dx, p2dy = -10, 0
        playing = True
        screen.fill((0,0,0))
    
    if playing:
        #DRAW P1
        p1x, p1y, p1dx, p1dy, = move(p1x, p1y, p1dx, p1dy, K_w, K_s, K_a, K_d, screen_bounds)
        p1trail.append([p1x, p1y])
        for i in range(len(p1trail)):
            drawSquares(screen, p1trail[i], RED)
        #DRAW P2
        p2x, p2y, p2dx, p2dy, = move(p2x, p2y, p2dx, p2dy, K_UP, K_DOWN, K_LEFT, K_RIGHT, screen_bounds)
        p2trail.append([p2x, p2y])
        for i in range(len(p2trail)):
            drawSquares(screen, p2trail[i], BLUE)

   
 #Collisions
        for x in cross:
            if [p1x, p1y] == x:
                playing = False
                print "Player1 lost"
            elif [p2x, p2y] == x:
                playing = False
                print "Player2 lost"


    #REFRESH
    cross.append([p1x, p1y])
    cross.append([p2x, p2y])
    pygame.display.flip()
    clock.tick(20)

