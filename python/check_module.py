import module as mmd
# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

mmd.greeting("Uvesh")
result = mmd.person1["age"]
print(result)

import platform
x = platform.system()
print(x) #windows



# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
from mymodule import person1





#  Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
# Example
# List all the defined names belonging to the platform module:
import platform
x = dir(platform)
print(x)

