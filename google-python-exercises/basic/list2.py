#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  index = 0
  while index < (len(nums) - 1):
    if nums[index] == nums[index + 1]:
      nums.pop(index + 1)
    else:
      index += 1
  return nums


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  if list1[0] <= list2[0]:
    katamari_list = list1        # I know this isn't a copy but I want a new name for this
    shrink_list = list2          # so katamari_list is what we'll add everything to
  else:
    katamari_list = list2
    shrink_list = list1

  kat_index = 0
  shrink_index = 0
  while len(shrink_list) > 0:
    # if there's only one thing left in katamari_list, don't just slop everything else on the end
    if len(katamari_list[kat_index:]) == 1 and katamari_list[kat_index] < shrink_list[shrink_index]:
      katamari_list.insert(kat_index-1, shrink_list[shrink_index])
      shrink_list.pop(0)
    # if our position in katamari_list has a smaller value than our current shrink_list position,
    # perfect; let's move on to the next value in katamari_list
    elif katamari_list[kat_index] < shrink_list[shrink_index]:
      kat_index += 1
    # if our position in katamari_list has a *larger* value, pop off the next shrink_list value
    # and plunk it in before the current kat_index
    else:
      katamari_list.insert(kat_index-1, shrink_list[shrink_index])
      # print 'about to pop'
      shrink_list.pop(0)

  return katamari_list













# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
