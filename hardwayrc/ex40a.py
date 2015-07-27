import mystuff

mystuffs = {'apple': "I AM APPLES!"} # deliberately adding s to avoid collision

mystuff.apple()
print mystuff.tangerine

mystuffs['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

thing = MyStuff()
thing.apple()
print thing.tangerine


# look at all these ways to get things from things:
# dict style
mystuffs['apple'] # also this sudden pluralization is interesting:
                  # it causes things to break here, & in the module/class ones

# module style
mystuff.apple()
print mystuff.tangerine

# class style
thing = MyStuff()
thing.apple()
print thing.tangerine