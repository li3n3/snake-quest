# our friend, the argv
# from sys import argv

# gives things to argv: the script name, and whatever filename was specified
# by the user
# script, filename = argv

# use raw_input instead of a command-line argument. it's a bummer to not be
# able to tab-complete the name of the file, but is a little clearer
print "What's the filename?"
filename = raw_input("> ")

# opens the specified file, but doesn't do anything with it yet
txt = open(filename)

print "Here's your file %r:" % filename
# okay so HERE'S the text of the file, though!
print txt.read()
