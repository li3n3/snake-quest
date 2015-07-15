from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from {0} to {1}".format(from_file, to_file)

indata = open(from_file).read()

# caution? more like YOLO
# print "The input file is {0} bytes long".format(len(indata))
#
# print "Does the output file exist? {0}".format(exists(to_file))
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
# in_file.close()