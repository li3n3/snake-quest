from sys import exit
import random


def start():
    """
    Welcome to Sluglife.
    You think to yourself, 'Yes, it is good to be a slug.' You set out.
    """
    print "\nYou find yourself on a garden path, dark and damp."
    print "There are three garden beds here: left, right, and center."
    print "Where would you like to crawl?"

    choice = raw_input("> ")

    if choice == "left":
        herb_garden()
    elif choice == "right":
        berries()
    elif choice == "center":
        vegetables()
    else:
        print "\nYou're just a slug, huh?"
        print "I'll pick for you."
        print "You squirm around in the air, finally hitting the ground with a thud."
        random.choice(gardens)()

def herb_garden():
    """
    An herb garden. It's got basil and a temperamental cat. So, a cat.
    """
    print "\nA fine aroma surrounds you."
    print "It appears you have found yourself in the herb garden."
    print "Regrettably, so has a cat."
    print "Do you turn around, hiss, or affix yourself to the cat?"

    choice = raw_input("> ")

    if "turn" in choice:
        start()
    elif choice == "hiss":
        demise("The cat notes your small size, hisses back, hits you, and eats you.")
    elif "affix" in choice:
        print "\nYou fling yourself at the cat's haunches, sticking your landing with ease."
        print "The cat does not appear to have detected your presence."
        print "Looks like you're hitching a ride..."
        plant_bounty("basil")
    else:
        print "\nI don't think that's such a good idea right now."
        print "Let's go over this again, okay?"
        herb_garden()


def berries():
    """
    So many berries. And a displeased gardener.
    """
    print "\nIn the dark, you see a beautiful brightness."
    print "All around you are berries, ripe and lushly scented."
    print "You realize with some horror that the brightness is a headlamp."
    print "There is a gardener here, searching for your kind."
    print "Do you run away, begin negotiations, or hide under a leaf?"

    choice = raw_input("> ")

    if "run" in choice:
        start()
    elif "begin" in choice or "negotiat" in choice:
        print "\nIn your most calm voice, you address the gardener."
        print "'I would like to propose a truce,' you say."
        print "'If you would give me some of your berries, I will stay away from the rest.'"
        print "The gardener considers this for a moment, finally plucking a plump ripe strawberry, then one more, and plunking them down next to you."
        plant_bounty("strawberries")
    elif "hide" in choice:
        print "\nYou hide underneath the nearest safe-looking strawberry plant."
        print "The gardener sweeps the light over the low shrubby leaves."
        print "With each pass, they check underneath the leaves toward the ground."
        print "At last, you are unearthed. The look on the gardener's face is not one of pity."
        demise("You are unceremoniously plucked from your hiding spot and plunged into a jar of soapy water, where you drown.")
    else:
        demise("This is not a time to be clever. A frog spies you pondering, and in a split second you are consumed.")


def vegetables():
    """
    Vegetables are here, but an owl is thinking about visiting here, too.
    """
    print "\nYou've arrived in a veritable forest of small leaves, juicy and full of potential."
    print "Vegetable starts as far as the eye can see."
    print "Over the tops of their tiny tips, you spy an owl in a nearby tree. Not good."
    print "What's more, the owl has clearly spied you. Uh oh."
    print "Do you flee, sing to the owl, or tell a knock-knock joke?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "sing" in choice:
        print "\nYou begin to sing a seemingly tuneless melody."
        print "The owl, intrigued, watches you intently."
        print "Out of your undulating foot-body comes a glorious, open vowel, rippling through the night air."
        print "The owl, inspired, joins in song with you. Owls, after all, love vowels. 'Hooo!' the owl calls."
        print "For a glorious moment in time, all seems perfectly in sync."
        print "The owl, overwhelmed by feelings, flies away, and you find yourself alone again."
        plant_bounty("radishes")
    elif "knock" in choice or "joke" in choice:
        print "\nIn your bravest voice, you say to the owl, 'knock knock.'"
        print "The owl, in turn, asks, 'Whooooo\'s there?'"
        print "You reply, 'a very cool and brave slug.'"
        print "The owl turns its head and says, 'Whooooo on earth do you think you are?'"
        print "As it turns out, owls do not like knock-knock jokes."
        demise("The owl makes a beeline for you, punishing your non-joke by eating you.")
    else:
        demise("The owl swoops down, pleased you've made yourself such an easy target, and swallows you whole.")


def plant_bounty(type_of_plant):
    """
    Yay, winning! Takes a type of plant to be eaten and lets you eat.
    But not if you hesitate.
    """
    print "Oh wow. What have we here? A terrific bounty of {0}.".format(type_of_plant)
    print "You're so hungry...finally, there is food."
    print "Do you eat the {0}?".format(type_of_plant)

    choice = raw_input("> ")

    if choice == "yes":
        print "\nSo good. You nibble a bit, then a bit more."
        print "It's so lovely to get a good meal."
        print "Covered in {0}, you slink away happily into the dark night.".format(type_of_plant)
        print "This was a good night to be a slug."
        exit(0)
    elif choice == "no":
        print "\nI know it's hard to accept, but you gotta destroy some things to live."
        print "But if you can't do that, I guess it's you who will be destroyed."
        demise("You remain still, frozen by your conscience, until the sun arrives and dries you up.")
    else:
        demise("It took too long to get here, it seems. You are too hungry to eat now, or ever again.")


def demise(reason):
    """
    Bad decisions (or a lack thereof) have led to your downfall.
    """
    print "\n{0} This was not such a good night.".format(reason)
    exit(0)

gardens = [herb_garden, vegetables, berries]

start()
