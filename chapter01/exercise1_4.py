# Exercise 1.4. Start the Python interpreter and use it as a calculator. Python’s syntax for math
# operations is almost the same as standard mathematical notation. For example, the symbols ✰, ✲ and
# ✴ denote addition, subtraction and division, as you would expect. The symbol for multiplication is
# ✯.
# If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What
# is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).

# total miles:
In [5]: (10 * (1/1.61))
Out[5]: 6.211180124223602

# average time per mile:
In [6]: 43.5 / (10 * (1/1.61))
Out[6]: 7.003500000000001

# okay whoops you're not running 270 miles per hour; 1 is the wrong numerator:
In [7]: (10 * (1/1.61)) / (1 / 43.5)
Out[7]: 270.1863354037267

# average speed in miles per hour:
In [8]: (10 * (1/1.61)) / (60 / 43.5)
Out[8]: 4.503105590062111