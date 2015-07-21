from sys import exit
import random


def start():
    print "You find yourself on a garden path, dark and damp."
    print "There are three garden beds here: left, right, and center."
    print "Where would you like to crawl?"

    choice = raw_input("> ")

    if choice == "left":
        herb_garden()
    elif choice == "center":
        annuals()
    elif choice == "right":
        perennials()
    else:
        print "You're just a slug, huh?"
        print "I'll pick for you."
        gardens[random.randint(0, 2)]

def herb_garden():
    print "A fine aroma surrounds you."
    print "It appears you have found yourself in the herb garden."


def annuals():
    print "eyyy the annuals are here"

def perennials():
    print "suppp it's perennials"

gardens = [herb_garden, annuals, perennials]

start()

# print "You think to yourself, 'Yes, it is good to be a slug.'"
