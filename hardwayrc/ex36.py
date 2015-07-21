from sys import exit
import random


def start():
    print "You find yourself on a garden path, dark and damp."
    print "There are three garden beds here: left, right, and center."
    print "Where would you like to crawl?"

    choice = raw_input("> ")

    if choice == "left":
        herb_garden()
    elif choice == "right":
        berries()
    elif choice == "center":
        annuals()
    else:
        print "You're just a slug, huh?"
        print "I'll pick for you."
        print "You squirm around in the air, finally hitting the ground with a thud."
        random.choice(gardens)()

def herb_garden():
    print "A fine aroma surrounds you."
    print "It appears you have found yourself in the herb garden."
    print "Regrettably, so has a cat."
    print "Do you turn around, hiss, or affix yourself to the cat?"

    choice = raw_input("> ")

    if "turn" in choice:
        start()
    elif choice == "hiss":
        demise("The cat notes your small size, hisses back, hits you, and eats you.")
    elif "affix" in choice:
        print "You fling yourself at the cat's haunches, sticking your landing with ease."
        print "The cat does not appear to have detected your presence."
        print "Looks like you're hitching a ride..."
        plant_bounty("basil")
    else:
        print "I don't think that's such a good idea right now."
        print "Let's go over this again, okay?"
        herb_garden()


def berries():
    print "In the dark, you see a beautiful brightness."
    print "All around you are berries, ripe and lushly scented."
    print "You realize with some horror that the brightness is a headlamp."
    print "There is a gardener here, searching for your kind."
    print "Do you run away, begin negotiations, or hide under a leaf?"

    choice = raw_input("> ")

    if "run" in choice:
        start()
    elif "negotiat" in choice:
        pass
        # then weirdly good stuff
    elif "hide" in choice:
        pass
        # unsuccessful demise stuff


def annuals():
    print "eyyy the annuals are here"


def plant_bounty(type_of_plant):
    """
    Yay, winning! Takes a type of plant to be eaten and lets you eat.
    """
    print "Hot diggity. An entire world of {0} surrounds you.".format(type_of_plant)
    print "You're so hungry...finally, there is food."
    print "Do you eat the {0}?".format(type_of_plant)

    choice = raw_input("> ")

    if choice == "yes":
        print "So good. You nibble a bit, then a bit more."
        print "It's so lovely to get a good meal."
        print "Covered in {0}, you slink away happily into the dark night.".format(type_of_plant)
        print "This was a good night to be a slug."
        exit(0)
    elif choice == "no":
        print "I know it's hard to accept, but you gotta destroy some things to live."
        print "But if you can't do that, I guess it's you who will be destroyed."
        demise("You remain still, frozen by your conscience, until the sun arrives and dries you up.")
    else:
        demise("It took too long to get here, it seems. You are too hungry to eat now, or ever again.")


def demise(reason):
    print reason, "This was not such a good night."
    exit(0)

gardens = [herb_garden, annuals, berries]

start()

# print "You think to yourself, 'Yes, it is good to be a slug.'"
