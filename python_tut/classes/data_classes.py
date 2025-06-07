"""Coding with Mosh Hamedani.

Author: Josh Borthick
Copying: Mosh Hamedani

Tricks for better code with data-only classes with no methods.  It is
possible to define the __eq__() magic method on a class to make sure
that its data can be tested for equality even though different objects
are stored in different memory locations and "==" checks for memory
location equality (which works fine for literals).  But this is some
extra, possibly unnecessary coding for a class which will only ever
hold data and have no functional methods.

This is where the namedtuple type comes in.  It allows the creation of
a type, creates a name for it, and allows comparison with "==".
"""

from collections import namedtuple

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# point1 = Point(1, 2)
# point2 = Point(1, 2)

# Would initially be False because the objects are each stored in 
# different memory locations, but would be True because __eq__ is
# defined.
# print(point1 == point2)

# Creates subclass of tuple with named fields and no class decl
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
