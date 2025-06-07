"""Coding with Mosh Hamedani.

Author: Josh Borthick
Copying: Mosh Hamedani

Built-in types and methods can be extended or overwritten by creating
classes which inherit from the type/object and add to or change their
methods.
"""

class Text(str):
    """A simple demonstration."""
    def duplicate(self):
        return self + self
    

class TrackableList(list):
    def append(self, value):
        """Calls the append method to add to list, but also logs it."""
        
        # This fails because max recursion depth reached
        # It calls itself, which then calls this method, then calls
        # itself again: infinite recursion without some safety trick
        # self.append(value)
        super().append(value)
        print("called append for", value)


lst = TrackableList()
lst.append("one")
