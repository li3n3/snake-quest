# first question:

In [36]: volume = (4/3) * 3.14 * (5**3)

In [37]: volume
Out[37]: 392.5

In [38]: 5**3
Out[38]: 125

In [39]: * 3.14
  File "<ipython-input-39-4742c29d6321>", line 1
    * 3.14
    ^
SyntaxError: invalid syntax


In [40]: 5**3 * 3.14
Out[40]: 392.5

In [41]: 392.5 * (4/3)
Out[41]: 392.5               # what the f

In [42]: 392.5 * (4.0/3)
Out[42]: 523.3333333333333


# second question
In [43]: 24.95 * .60
Out[43]: 14.969999999999999

In [44]: bookstore_price = 24.95 * .60

In [45]: (60 * book
%bookmark        bookstore_price  

In [45]: (60 * bookstore_price) + (3 + .75 * 59)
Out[45]: 945.4499999999999


# third question:
In [46]: 12/60    # oh yeah floors
Out[46]: 0

In [47]: 12.0/60  # what's twelve minutes, expressed in decimal format?
Out[47]: 0.2

In [48]: 8.25 + 3 * 7.2 + 8.25   # lazy "8:15 + 3 times 7:12 + 8:15" minute addition
Out[48]: 38.1                    # so it takes 38.1 minutes

In [49]: .1 * 60                 #...how much is .1 minutes? it's six seconds. oh. right.
Out[49]: 6.0

In [50]: 52 + 38.1               # leaving at 6:52, adding 38.1 minutes...
Out[50]: 90.1

In [51]: 90.1 - 60               # but then removing the extra sixty to get a clock-time
Out[51]: 30.099999999999994

# so, 7:30 am?