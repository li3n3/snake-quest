#RC day 2
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

# draw square with a for loop!
for i in range(4):
    fd(bob, 100)
    lt(bob)

wait_for_user()