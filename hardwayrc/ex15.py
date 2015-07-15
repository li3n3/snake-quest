# our friend, the argv
from sys import argv

# gives things to argv: the script name, and whatever filename was specified
# by the user
script, filename = argv

# opens the specified file, but doesn't do anything with it yet
txt = open(filename)

print "Here's your file %r:" % filename
# okay so HERE'S the text of the file, though!
print txt.read()
