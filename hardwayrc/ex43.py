from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene isn't configured yet. Subclass it and implement"\
        " enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # but don't forget to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died.  Not so good at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luuuuuuser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        print "Gothons. Such a freaking bummer, how they've infested your ship"
        print "and destroyed all your friends. Boo."
        print "You're the only one left. Your mission is to get the neutron"
        print "bomb from the Weapons Armory, put it in the bridge, and blow"
        print "the ship up after getting into an escape pod."
        print "Come on, don't look so sad. It's not like anyone else will know"
        print "if you fail."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory"
        print "when a Gothon jumps out, shimmering scaly skin, sludge-covered"
        print "teeth, and a cloud of wasps manifesting the pure hate of his"
        print "heart. He's barricading the door to the Armory and he's"
        print "reaching for his weapon..."

        action = raw_input("> ")

        if action == "shoot!":
            print "Swiftly, you pull out your blaster and fire it at the Gothon."
            print "The wasps are swarming around him, and now at you, and while"
            print "you see a lot of them go up in a buzzing smoke, you don't"
            print "appear to have hit the Gothon at all. The wasps and the"
            print "Gothon, being terrifically irritated at this point, sting"
            print "and shoot you to pieces, respectively."
            return 'death'

        elif action == "dodge!":
            print "Such art. Many dodge."
            print "You swoop first to one side, then to another, and then..."
            print "to another, and another, and another..."
            print "There is no end to your world of dodging, and you dodge"
            print "right into an open elevator shaft, where you plunge to your"
            print "demise. The Gothon fires a final shot downward, just to be"
            print "sure you've met your end."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you, they made you learn Gothon insults in the"
            print "academy. A single one comes to mind:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur"
            print "fvgf nebhaq gur ubhfr."
            print "The Gothon is powerless to disacknowledge your wordplay."
            print "He bursts into peals of laughter, unable to open his eyes,"
            print "so you run up and handily shoot him in the head, hopping"
            print "through the Weapon Armory door right after."
            return 'laser_weapon_armory'

        else:
            return "DOES NOT COMPUTE!"
            return 'central_corridor'


class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()

# left off partway through, because boredom is my enemy at RC
