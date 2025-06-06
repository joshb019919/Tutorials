"""Coding with Mosh Hamedani.

Author: Josh Borthick
Copying: Mosh Hamedani 

Explaining inheritance.  Class inheritance allows the subclassing of
other classes, making it so these subclasses can inherit all their
parent's methods and properties, but also have their own.  It also
lets code stay DRY with reusability, but it can be abused.  For
example, it's good to stick to one or two levels of classes, not
trying to model the entire universe as this increases complexity in
the code.
"""

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self, food):
        print("is eating", food)


class Mammal (Animal):
    # Will override Animal.age, making calls to print(dog.age), etc.,
    # fail because now, Animal.age is no longer defined
    # def __init__(self):
    #     self.weight = 3

    # Will allow Animal.age as well as Mammal.weight because of super()
    def __init__(self):
        # This calls the Animal constructor before the rest of the
        # Mammal constructor; could be other way around, too
        super().__init__()
        self.weight = 3

    def walk(self):
        print("is walking")


class Fish (Animal):
    def swim(self):
        print("is swimming")


class Clownfish(Fish):
    """Example of too much inheritance."""
    pass


class AdultClownfish(Clownfish):
    """Example of too much inheritance."""
    pass


dog = Mammal()
dog.eat("rabbit")     # "is eating rabbit"
dog.walk()            # "is walking"
print("dog is", dog.age, "years old")    # "1"

nemo = Fish()
nemo.eat("plankton")  # "is eating plankton"
nemo.swim()           # "is swimming"
print("nemo is", nemo.age, "years old")  # "1"

# Check if one object is instance of a certain type
print(isinstance(dog, Mammal))  # True
print(isinstance(dog, Animal))  # True
print(isinstance(dog, object))  # True

# Check if one class is a subclass of (Type or Type or Type...)
print(issubclass(Fish, Mammal))                    # False
print(issubclass(Fish, (Mammal, Animal, object)))  # True
