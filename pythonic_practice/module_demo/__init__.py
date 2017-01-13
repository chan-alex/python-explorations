


# Code in this file gets executed when the modules in this package are imported.
print("Hello, from __init__.py")


# it is common use this file to import modules need by the other modules.
from .module2 import global_var2

print(global_var2)
