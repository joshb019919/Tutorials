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
dog.eat("rabbit")  # "is eating rabbit"
dog.walk()         # "is walking"

nemo = Fish()
nemo.eat("plankton")  # "is eating plankton"
nemo.swim()           # "is swimming"

# Check if one object is instance of a certain type
print(isinstance(dog, Mammal))  # True
print(isinstance(dog, Animal))  # True
print(isinstance(dog, object))  # True

# Check if one class is a subclass of (Type or Type or Type...)
print(issubclass(Fish, Mammal))                    # False
print(issubclass(Fish, (Mammal, Animal, object)))  # True
