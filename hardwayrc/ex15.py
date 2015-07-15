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

print "Type the filename again:"
# getting the same filename in a different way (via raw_input,
# and not via arguments given at runtime)
file_again = raw_input("> ")

# open the same file and assign it to a second variable
txt_again = open(file_again)

# print the file from the second variable
print txt_again.read()