"""Coding with Mosh Hamedani.

Author: Josh Borthick
Copying: Mosh Hamedani

This is a good example of inheritance.  Both FileStream and
NetworkStream inherit from Stream class, as different sources for
streams need different implementations, but both need the same 
basic setups for opening and closing the stream.  

This example utilizes abstraction of methods and classes.  In Python,
abstract classes or classes with abstract methods cannot be
instantiated.  

There is also a custom exception class defined.  It inherits from the
base Exception class (not to be confused with the BaseException
class).  It defines nothing as everything is implemented in Exception.
"""

from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened == True:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True
        
    def close(self):
        if self.opened == False:
            raise InvalidOperationError("Stream is already closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading from a network.")


class MemoryStream(Stream):
    pass


# Cannot instantiate abstract class Stream
# stream = Stream()
# Cannot instantiate abstract class MemoryStream
stream = MemoryStream()

fstream = FileStream()
fstream.open()
fstream.read()

nstream = NetworkStream()
nstream.open()
nstream.read()
