#!/usr/bin/env python


###########
import pygame
from pygame.locals import *

screen_size=640,480
background=0,0,0

#init pygame
pygame.init()
screen=pygame.display.set_mode(screen_size)

done=False
while not done:
    event = pygame.event.poll()

    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True
    elif event.type == KEYDOWN and event.key == K_w:
        background=255,255,255
    elif event.type == MOUSEBUTTONDOWN:
        print "Mouse",pygame.mouse.get_pos()

    screen.fill(background)
    pygame.display.flip()

print "KTHXBYE LOL"
#############

############
#name_in=raw_input("Enter a name.  ")
#
#if name_in == "Paul":
#    print "you are cool.  "
#elif name_in == "Alec" or name_in == "Jonah" or name_in == "Jack":
#    print "you smell bad."
#else:
#    print "you need some learnin'"
############
