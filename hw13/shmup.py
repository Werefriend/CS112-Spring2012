#!/usr/bin/env python

import random
import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group, GroupSingle
import os, sys

#some variables...
BLACK =0,0,0
WHITE = 255,255,255
SCREEN_SIZE = 600,600
MYSTERIOUS_GREEN = 0x0ffd03
FPS = 30


#importing images!!!1!                                                                     
def ld_pics(filename, colorKey=None):
    pthnm = os.path.join('pics', filename)
    try:
        image = pygame.image.load(pthnm)
    except pygame.error, message:
        print 'Cannot load', pthnm
        raise SystemExit, message
    image = image.convert()
    if colorKey is not None:
        if colorKey is -1:
            colorKey = image.get_at((0,0))
        image.set_colorkey(colorKey, RLEACCEL)
    return image, image.get_rect()

#making some texts for the screens
def text_render(text, x, y, color, size):
    font = pygame.font.Font(None, size)
    rend = font.render(text, True, color)
    screen.blit(rend, (x, y))

#this makes the player's sprite!
class PlayerShip(Sprite):
    def __init__(self, x, y, bounds):
        Sprite.__init__(self)
        self.image, self.rect = ld_pics('ship.bmp')
        self.rect.x = x
        self.rect.y = y
        self.dx = 0
        self.dy = 0
        self.bounds = bounds
        self.bullets = Group()

    def shoot(self):
        bullet = Bullet(self.rect.x, self.rect.y, self.bounds)
        self.bullets.add(bullet)

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left < self.bounds.left:
            self.rect.left = self.bounds.left
        if self.rect.right > self.bounds.right:
            self.rect.right = self.bounds.right

#makin burgers LOL        
class Burger(Sprite):
    def __init__(self, x, y, bounds):
        Sprite.__init__(self)
        self.image, self.rect = ld_pics('burger.bmp')
        self.rect.x = x
        self.rect.y = y
        self.dx = random.randrange(-10, 10)
        self.dy = random.randrange(1, 10)
        self.bounds = bounds
        

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.dx *= -1
            self.rect.x += self.dx*2
        if self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.dy *= -1
            self.rect.y += self.dy*2

    def kill(self):
        burger2 = Burger(self.rect.x, self.rect.y, self.bounds)
        burger3 = Burger(self.rect.x, self.rect.y, self.bounds)

        for group in self.groups():
            group.add(burger2)
            group.add(burger3)

        Sprite.kill(self)

#makin weiners LOL
class Hotdog(Sprite):
    def __init__(self, x, y, bounds):
        Sprite.__init__(self)
        self.image, self.rect = ld_pics('hotdog.bmp')
        self.rect.x = x
        self.rect.y = y
        self.dx = random.randrange(-10,10)
        self.dy = random.randrange(1,10)
        self.bounds = bounds
        
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.dx *= -1
            self.rect.x += self.dx*2
        if self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.dy *= -1
            self.rect.y += self.dy*2

class Bullet(Sprite):
    def __init__(self, x, y, bounds):
        Sprite.__init__(self)
        self.image, self.rect = ld_pics('bullet.bmp')
        self.rect.x = x
        self.rect.y = y
        self.bounds = bounds
        
    def update(self):
        self.rect.y -= 10
        if self.rect.top < self.bounds.top:
            self.kill()

## Game
def game():
    # init
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    dude = PlayerShip(260, 500, screen.get_rect())
    dude_grp = GroupSingle(dude)
    enemies = Group()
    enemies.add(Burger(200, 200, screen.get_rect()))
    enemies.add(Hotdog(100, 100, screen.get_rect()))

    #loop
    while True:
        # input
        for evt in pygame.event.get():
            if evt.type == QUIT:
                return
            elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
                return
            elif evt.type == KEYDOWN and evt.key == K_a:
                dude.dx = -10
            elif evt.type == KEYDOWN and evt.key == K_d:
                dude.dx = 10
            elif evt.type == KEYUP and evt.key == K_a and dude.dx == -10:
                dude.dx = 0
            elif evt.type == KEYUP and evt.key == K_d and dude.dx == 10:
                dude.dx = 0
            elif evt.type == KEYDOWN and evt.key == K_SPACE and dude.alive():
                dude.shoot()
                
        # update
        clock.tick(FPS)
        dude.update()
        enemies.update()
        dude.bullets.update()

        pygame.sprite.groupcollide(enemies, dude.bullets, 1, 1)
        pygame.sprite.groupcollide(dude_grp, enemies, 1, 0)

        # draw
        screen.fill(BLACK)
        dude_grp.draw(screen)
        enemies.draw(screen)
        dude.bullets.draw(screen)
        pygame.display.flip()
        
game()
