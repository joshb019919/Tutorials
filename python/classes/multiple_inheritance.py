"""Coding with Mosh Hamedani.

Author: Josh Borthick
Copying: Mosh Hamedani

Classes can inherit from multiple other classes, but things can get
complicated.  Python's interpreter deals with reference inheritance
very specifically: if a variable's definition is not found within the
class for which it is needed and it has inherited classes, the 
interpreter will check each parent class, in order, till it finds at
least one definition.  It will stop looking there, so that other parent
classes are never checked.

Bad usage of multiple inheritance involves inheriting from classes
which have things in common.  Good usage is where they don't.
"""


class Employee:
    def greet(self):
        print("From Employee!")


class Person:
    def greet(self):
        print("From Person...")


class Manager(Person, Employee):
    pass


manager = Manager()
manager.greet()  # "From Person..." because Person class is first in the list.
