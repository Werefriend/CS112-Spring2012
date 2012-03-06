#!/usr/bin/env python

import pygame
from pygame.locals import *

#globals
BACKGROUND = (80, 80, 80)
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (800, 600)
FPS = 30
RECT_SIZE = (120, 80)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

bounds = screen.get_rect()
rects = [ pygame.Rect((0, 0), RECT_SIZE),
          pygame.Rect((0, 0), RECT_SIZE),
          pygame.Rect((0, 0), RECT_SIZE),
          pygame.Rect((0, 0), RECT_SIZE) ]

rects[0].topleft = bounds.topleft
rects[1].topright = bounds.topright
rects[2].bottomleft = bounds.bottomleft
rects[3].bottomright = bounds.bottomright

bigfont = pygame.font.Font(None, 80)


grabbed = False

done = False

while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True
        elif evt.type == MOUSEBUTTONDOWN:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()):
                    grabbed = rect
            #move grabbed rect to top
            if grabbed:
                rects.remove(grabbed)
                rects.append(grabbed)

        elif evt.type == MOUSEBUTTONUP:
            grabbed = None

        if grabbed:
            grabbed.center = pygame.mouse.get_pos()
            grabbed.clamp_ip(bounds)

    #DRAW
    screen.fill(BACKGROUND)
    text = bigfont.render("Drag the rectangles", True, (0, 0, 0), BACKGROUND)
    loc = text.get_rect()
    screen.blit(text, loc)
    for rect in rects:
        others = rects[:]
        others.remove(rect)

        if grabbed:
            color = WHITE
        elif rect.collidelist(others) != -1:
            color = GREEN
        else:
            color = RED
    
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 5)
        
    #REFRESH
    pygame.display.flip()
    clock.tick(FPS)
