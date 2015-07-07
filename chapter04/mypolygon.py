#RC day 2
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.2

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
        lt(t, 360/n)

def circle(t, r):
    '''
    t: a Turtle
    r: a radius
    Draws an approximate circle with the given radius
    '''
    # circumference = 2 * pi * r
    circ = 2 * 3.14 * r
    # TODO: figure out a better way to determine number of sides
    n = 36
    length = circ / n
    return polygon(t, length, n)

# skipping 4.3 exercise 5



# square(bob, 42)

# so, for instance, this draws a 5-sided polygon, with sides of
# length 80
# polygon(bob, 80, 5)

# circle! approximate circle, anyway
circle(bob, 95)

wait_for_user()