name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.54
weight = 180 # lbs
weight_kg = weight * 0.454
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# skipping %s in favor of more awesome/newer .format
print "Let's talk about {0}.".format(name)
print "He's {0} inches tall.".format(height)
print "(That's {0} centimeters.)".format(height_cm)
print "He's {0} pounds heavy.".format(weight)
print "(Which is {0} kilograms.)".format(weight_kg)
print "Actually that's not too heavy."
print "He's got {0} eyes and {1} hair.".format(eyes, hair)
print "His teeth are usually {0} depending on the coffee.".format(teeth)

# this line is tricky, try to get it exactly right
print "If I add {0}, {1}, and {2} I get {3}.".format(age, height, weight, age + height + weight)
