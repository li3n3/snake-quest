#RC day 2
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

# draw a right angle
fd(bob, 100)
lt(bob)
fd(bob, 100)

# continue going to complete a square
lt(bob)
fd(bob, 100)
lt(bob)
fd(bob, 100)

for i in range(4):
    print 'Hello!'

wait_for_user()