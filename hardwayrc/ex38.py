ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
# python does split(ten_things, ' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    # python does pop(more_stuff)
    print "Adding: ", next_one
    stuff.append(next_one)
    # python does append(stuff, next_one)
    print "There are {0} items now.".format(len(stuff))
    # oooh; this would be interesting to rephrase
    # maybe? format("There are {0} items now.", len(stuff))

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
# python does pop(stuff)
print ' '.join(stuff) # what? cool!
# python does join (' ', stuff)
print "#".join(stuff[3:5]) # super stellar!
# python does join('#', stuff[3:5])
