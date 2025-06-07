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
package within the whole program, and will include modules, thusly.
"""

# Find module search path
import sys
print(sys.path)


