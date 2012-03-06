#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""
import pygame
from pygame import Rect
from pygame import *

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False

def poly_in_rect(poly, rect):
    "check if polygon is within rectangle"
    inscribed = True
    for corner in poly:
        x,y = corner 
        if rect.collidepoint(x,y) == True:
            inscribed = True
        else:
            inscribed = False
            break
    return inscribed


# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect

def surround_poly(poly):
    "create a rectangle which surounds a polygon"

    x,y = poly[0]
    xmin = x
    xmax = x
    ymin = y
    ymax = y

    for corner in poly[1:]:
        x,y = corner
        if xmax < x:
            xmax = x
        elif xmin > x:
            xmin = x

        if ymax < y:
            ymax = y
        elif ymin > y:
            ymin = y
    return pygame.Rect((xmin, ymin), (xmax -xmin +1, ymax -ymin +1))
