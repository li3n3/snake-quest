#RC day 2
from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
alice = Turtle()
bob.delay = 0.01

# draw square with a for loop!
# for i in range(4):
#     fd(bob, 100)
#     lt(bob)

def square(t, length):
    '''
    t: a Turtle
    length: the length of each side
    Turtle draws a square with specified side length
    '''
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    '''
    t: a Turtle
    length: the length of each side
    n: number of sides
    Turtle draws a polygon with specified side length
    '''
    for i in range(n):
        fd(t, length)
        lt(t, 360.0/n)

def circle(t, r):
    '''
    t: a Turtle
    r: a radius
    Draws an approximate circle with the given radius
    '''
    # circumference = 2 * pi * r
    circ = 2 * math.pi * r
    # use a reasonable number of sides; I don't entirely get the +1
    n = int(circ / 3) + 1
    length = circ / n
    polygon(t, length, n)

# skipping 4.3 exercise 5



# square(bob, 95)

# so, for instance, this draws a 5-sided polygon, with sides of
# length 80
# polygon(bob, 80, 5)

# circle! approximate circle, anyway
circle(bob, 95)
circle(alice, 30)

wait_for_user()