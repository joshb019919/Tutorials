"""Coding with Mosh Hamedani.

Author: Josh Borthick
Copying: Mosh Hamedani

Polymorphism is very powerful.  The second draw function does not need
to know the type of the control to draw, it just needs passed the list.

It's the same concept for Python's "duck typing" functionality.  If the
UIControl abstract class were to be removed, the draw function would 
still work fine, because Python doesn't check type even between the
different items of the same list.  They can be completely different 
types or objects and it will run, just fine.
"""

from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Drawing TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("Drawing DropDownList")


# def draw(control):
#     """Original draw function."""
#     control.draw()


def draw(controls):
    """List draw."""
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()
print(isinstance(ddl, DropDownList))
print(isinstance(ddl, UIControl))
# ddl.draw()
# draw(ddl)

draw([ddl, tb])
