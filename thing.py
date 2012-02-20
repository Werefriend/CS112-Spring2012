#!/usr/bin/env python

import pygame
from pygame.locals import *
from pygame import gfxdraw


SCREEN_SIZE = 640, 480
FPS = 30

screen = None
player = Rect(0, 0, 16, 16)
bounds = Rect(0, 0, 200, 200)

def center_mouse():
    x,y = screen.get_rect().center
    pygame.mouse.set_pos(x,y)
    pygame.mouse.get_pos(x,y)

def update():
    x,y = pygame.mouse.get_rel()
    player.move_ip(x,y)
    if not bounds.contains(player):
        player.center = bounds.center
        center_mouse()


def draw(surf):
    surf.fill((80, 80, 80))
    surf.fill((0, 0, 0), bounds)
    surf.fill((255, 0, 0), player)




def run():
    # initialize everything
    global screen
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF|HWSURFACE)
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()

    #center the bounds
    bounds.center = screen.get_rect().center

    #center bounds
    bounds.center = screen.get_rect().center


    #game loop
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True

        update()
        draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    run()
    print "Bye bye"
