#RC day 2
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

# draw square with a for loop!
for i in range(4):
    fd(bob, 100)
    lt(bob)

def square(t):
    '''
    takes a parameter t, a Turtle
    uses that turtle to draw a square
    '''
    for i in range(4):
        fd(t, 100)
        lt(t)

square(bob)

wait_for_user()