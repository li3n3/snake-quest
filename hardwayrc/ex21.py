def add(a, b):
    print "ADDING {0} + {1}".format(a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING {0} - {1}".format(a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING {0} * {1}".format(a, b)
    return a * b

def divide(a, b):
    print "DIVIDING {0} / {1}".format(a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: {0}, Height: {1}, Weight: {2}, IQ: {3}".format(
    age, height, weight, iq)

# A puzzle for the extra credit; type it in anyway.
print "Here is a puzzle."

what = divide(age, subtract(height, multiply(weight, add(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"