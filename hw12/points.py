#!/usr/bin/env python
import math
from math import *

# Point Object
# =====================================
# Create a Point point class.  Point objects, when created, look like this:
#     >>> pt = Point(3,4)
#     >>> print pt.x
#     3
#     >>> print pt.y
#     4
#
# In addition points have the following methods:
#    distance(self, other):
#        calculates the distance between this point and another
#    
#    move(self, x, y):
#        sets the points location to x,y
# 
#    translate(self, x, y):
#        offsets the point by x and y
# 
#    When all done, points should work like this:
#
#    >>> a = Point(0,0)
#    >>> b = Point(0,0)
#    >>> b.move(2, 2)
#    >>> print b.x, b.y
#    2 2
#    >>> b.translate(1,2)
#    >>> print b.x, b.y
#    3 4
#    >>> print a.distance(b)
#    5
#

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == self.y:
            return True
        else:
            return False

    def __str__(self):
        ptstr = "(" + self.x + "," + self.y + ")"
        return ptstr

    def distance(self, other):
        xsq = (self.x - other.x)**2
        ysq = (self.y - self.y)**2
        dist = math.sqrt(xsq + ysq)
        return dist

    def move(self, x, y):
        self.x = x
        self.y = y

    def translate(self, x, y):
        self.x += x
        self.y += y

    def slope(self, other):
        sl = (self.y - other.y) / (self.x / other.X)
        if sl < 0:
            sl *= -1
        return sl

    def extrapolate(self, slope, distance):
        self.slope = slope
        self.distance = distance
        xdist = dist / slope
        ydist = dist * slope
        newx = xdist + self.x
        newy = ydist + self.y
        newpoint = (newx, newy)
        return newpoint

# Advanced Section:
# ---------------------------------------
# Add the following function:
#     slope(self, other):
#         calculate the slope between two points
#
#     extrapolate(self, slope, distance):
#         returns a point along the line defined by slope
#         a given distance away
#
# Also, add the following special python methods:
#     __eq__(self, other):
#         checks if other is a Point and is equal to self
#
#     __str__(self):
#         returns a string representation of the point 
#     
#     >>> print Point(3,4)
#     (3,4)
#     >>> a = Point(1,2)
#     >>> b = Point(1,2)
#     >>> print a == b
#     True
