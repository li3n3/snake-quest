from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

joke = raw_input("Tell me a joke. ")
print "Ha ha! Oh wow. And only {0} characters long.".format(len(joke))