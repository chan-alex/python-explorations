

# Python functions are actually objects.

def add1(x):
    return x + 1


# Because functinos are object, it is possible to set arbitrary attributes on them
add1.some_var = 5
print("add1.some_var = {}".format(add1.some_var))

# functions also have some attributes defined by default such as:
print("add1.__name__ = {}".format(add1.__name__))
print("add1.__class__ = {}".format(add1.__class__))
