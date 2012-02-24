#!/usr/bin/env python

import pygame
from pygame import draw
from random import randrange
from pygame.locals import *

tie_x, tie_y = 400,300

def draw_tie(surf, pos, color=(255,0,0), size=40):
    "Draws a tie fighter"
    x,y = pos
    
    width = size/8

    draw.rect(surf, color, (x, y, width, size))
    draw.rect(surf, color, (x+(size-width), y, width, size))
    draw.rect(surf, color, (x, y+(size-width)/2, size, width))
    draw.circle(surf, color, (x+size/2, y+size/2), size/4)


def move(x, y, dx, dy, bounds):
    x += dx
    y += dy
    if x-40 < bounds.left or x+40 > bounds.right:
        x += dx*2
        dx += 3
        dx *= -1
    if y-40 < bounds.top or y+40 > bounds.bottom:
        y += dy*2
        dy += 3
        dy *= -1
    return x, y, dx, dy

ties = []
color = []
pygame.init()
dx = 1
dy = 1
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
screen_bounds = screen.get_rect()
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
    
    # update
    tie_x, tie_y, dx, dy = move(tie_x, tie_y, dx, dy, screen_bounds)
    ties.append([tie_x,tie_y])
    color.append(255)

    # trim trail
    if len(ties) > 255:
        ties.pop(0)
        color.pop(0)

    # draw
    screen.fill((0,0,0))
    for i in range(len(ties)):
        color[i] -= 1
        draw_tie(screen, ties[i],(color[i],color[i],color[i]))

    
    pygame.display.flip()
    clock.tick(60)
    
print "ByeBye"
