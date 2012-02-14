#!/usr/bin/env python

import math
import pygame
from pygame.locals import *

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

## Draw
screen.fill(WHITE)

#################################
##  DRAW OLYPIC RINGS HERE
##
##  hint, lookup pygame.draw
##  specifically circle, ellipse,
##  and arc.  Also, the width
##  parameter
#################################

#order of circles: blue,yellow,black,green,red

pygame.draw.circle(screen,BLUE,(135,135),120,22)
pygame.draw.circle(screen,YELLOW,(270,250),120,22)
pygame.draw.circle(screen,BLACK,(405,135),120,22)
pygame.draw.circle(screen,GREEN,(540,250),120,22)
pygame.draw.circle(screen,RED,(675,135),120,22)

pygame.draw.arc(screen,WHITE,(15,15,248,248),math.radians(340),math.radians(390),38)
pygame.draw.arc(screen,BLUE,(15,15,240,240),math.radians(330),math.radians(390),22)

pygame.draw.arc(screen,WHITE,(144,127,248,248),math.radians(140),math.radians(200),34)
pygame.draw.arc(screen,YELLOW,(150,130,240,240),math.radians(140),math.radians(240),22)
pygame.draw.arc(screen,WHITE,(144,125,248,248),math.radians(60),math.radians(87),34)
pygame.draw.arc(screen,YELLOW,(150,130,240,240),math.radians(60),math.radians(90),22)

pygame.draw.arc(screen,WHITE,(279,13,248,248),math.radians(220),math.radians(270),34)
pygame.draw.arc(screen,BLACK,(285,15,240,240),math.radians(220),math.radians(270),22)
pygame.draw.arc(screen,WHITE,(282,15,248,248),math.radians(-18),math.radians(15),34)
pygame.draw.arc(screen,BLACK,(285,15,240,240),math.radians(-22),math.radians(17),22)

pygame.draw.arc(screen,WHITE,(415,127,248,248),math.radians(140),math.radians(200),34)
pygame.draw.arc(screen,GREEN,(420,130,240,240),math.radians(140),math.radians(240),22)
pygame.draw.arc(screen,WHITE,(415,125,248,248),math.radians(60),math.radians(87),34)
pygame.draw.arc(screen,GREEN,(420,130,240,240),math.radians(57),math.radians(90),22)

pygame.draw.arc(screen,WHITE,(555,15,248,248),math.radians(220),math.radians(270),34)
pygame.draw.arc(screen,RED,(555,15,240,240),math.radians(220),math.radians(273),22)

#YEAH GET SOME


## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
