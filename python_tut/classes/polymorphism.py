"""Coding with Mosh Hamedani.

Author: Josh Borthick
Copying: Mosh Hamedani


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


ddl = DropDownList()
print(isinstance(ddl, DropDownList))
print(isinstance(ddl, UIControl))
ddl.draw()
