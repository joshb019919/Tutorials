"""Code with Mosh Hamedani.

Author: Josh Borthick
Following along with: Mosh Hamedani

Compiled Modules
When needing to import a custom-written module into another custom
Python script, Python interpreter will actually compile the imported
script to speed up module loading (but not execution speed).  Python
will then check the difference between the compiled version and the 
source code version to make sure it has the latest version to load.
It always freshly interprets the script which is loaded explicitly
via command line or other executing means, so that script is never
compiled.

Module Search Path
When looking for an imported module, Python looks in a host of
different places, which can be found like the below.

Creating Packages
Python considers any subdirectory of a working directory with a file
called __init__.py contained within it as a package of the whole
"program" full of Python scripts.  Normally, Python can't find modules
in subdirectories without being specifically told where they are, but
puting an init file in there, even if empty, informs Python that the
directory contains scripts to be considered modules as part of a 
package within the whole program.  

To call modules in packages, import as usual, but from package_name.
module_name.

Subpackaging
Subpackaging works just like importing packages.  Include a file called
__init__.py and import it from outer_package.inner_package.module_name.

Absolute & Relative Imports
Absolute imports as as usual, going from package to subpackage till
finding the desired module, class, or function to import.  Relative
imports utilize the "..outer_package.sibling_package" notation to go 
back from a given location to further and further outer packages.

dir Function
The "dir" function shows all the attributes defined on an object, such
as magic attributes (e.g., __name__ or __package__) and regular 
attributes.  This can help in debugging.

Exporting Modules as Scripts
The executing file is always called __main__, which is why if __name__
== "__main__" only executes stuff when the module with that conditional
is interpreted.  If it is interpreted as part of being imported by
another module, that part will not execute.  Things like print 
statements in imported modules which are NOT in such conditionals are
executed when the module is imported.  This can be a useful trick to
show things such as when a module has been started.  Putting such a
print call in an __init__ file can show when a package has been
initialized.  Modules which are not named __main__ are named by their
package path.
"""

# Find module search path
import sys
print(sys.path)  # Prints path names

# Absolute and relative imports
from inner.more_inner.mod import more_inner_function

#Neither of these work since __package__ is obviously not defined
# from .inner.not_a_package.mod import not_a_package_function
# from ..classes.polymorphism import ddl

# Can't find this function since not_a_package has no __init__.py
# from inner.not_a_package.mod import not_a_package_function

# not_a_package_function()
more_inner_function()  # "more_inner function"

# Shows a bunch of attributes of the __package__ attribute.
# print(dir(__package__))
