"""Code with Mosh Hamedani.

Author: Josh Borthick
Following along with: Mosh Hamedani

Path objects can be used from pathlib library.
"""

from pathlib import Path

# Create path objects from strings
print(Path(r"C:\Program Files\Git"))                    # Windows-based path
print(Path("/usr/src/linux-headers-6.11.0-35-common"))  # Unix/Linux-based path

# The current path at execution
print(Path())

# Relative path from current
print(Path("stl/path_objects.py"))

# Another way to do it
print(Path() / "stl" / "path_objects.py")

# Path to home dir
print(Path.home())

############ Useful Methods #############
print()
path = Path(r"C:\Users\User\.ssh\id_ed25519.pub")
print(f"Path {path} exists? {path.exists()}")
path = Path("/home/jborthick/.ssh/id_ed25519.pub")
print(f"Path {path} exists? {path.exists()}")
print(f"Path is file? {path.is_file()}")
print(f"Path is directory? {path.is_dir()}")
print(f"Path name: {path.name}")
print(f"Path name without extension: {path.stem}")
print(f"Path extension name: {path.suffix}")
