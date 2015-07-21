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
        perennials()
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

def perennials():
    print "suppp it's perennials"

def annuals():
    print "eyyy the annuals are here"


def demise(reason):
    print reason, "This was not such a good night."
    exit(0)

gardens = [herb_garden, annuals, perennials]

start()

# print "You think to yourself, 'Yes, it is good to be a slug.'"
