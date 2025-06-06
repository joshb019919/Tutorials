"""Coding with Mosh Hamedani.

Author: Josh Borthick
Copying: Mosh Hamedani 

Explaining inheritance.  Class inheritance allows the subclassing of
other classes, making it so these subclasses can inherit all their
parent's methods and properties, but also have their own.
"""

class Animal:
    def eat(self, food):
        print("is eating", food)


class Mammal (Animal):
    def walk(self):
        print("is walking")


class Fish (Animal):
    def swim(self):
        print("is swimming")


dog = Mammal()
dog.eat("rabbit")
dog.walk()

nemo = Fish()
nemo.eat("plankton")
nemo.swim()
