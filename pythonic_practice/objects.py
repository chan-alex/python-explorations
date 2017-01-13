

# Creating classes

# class ClassName:
#  suite

# class ClassName(base_classes):
#  suite

# This is the absolute minium class definition
class MinimalClass:
    pass   # sames "move along, nothing to see here."

# This is how to create a new object:

a = MinimalClass()
b = MinimalClass()

print(a)
print(b)

# <__main__.MinimalClass object at 0x1079203c8>
# <__main__.MinimalClass object at 0x107920470>


# Even with this minimal class, it is possible to add attribute to it.

a.x = 10
a.y = 11


# Adding methods
class RealNumber:
    def reset(self):   # Python method always have a "self" argument.
        self.num = 0


r1 = RealNumber()

r1.num = 10
print(r1.num)
r1.reset()
print(r1.num)


# About the self argument is simply a reference to the object being invoked on.

r1.num = 100
RealNumber.reset(r1)  # same as r1.reset()

r2 = RealNumber()
r2.num = 200
RealNumber.reset(r2)  # same as r1.reset()



# Initializing an object
# The __init__ method is the way to initialize an object


class RealNumber:
    def __init__(self, number=0):
        self.num = number

r1 = RealNumber()
print(r1.num)


# The thing to note is that __init__ is actually called after __new__.
# But usually you only need to just define __init__.

class RealNumber:
    def __new__(self):
        print("Hi there, this is from __new__")

    def __init__(self, number=0):
        self.num = number


r1 = RealNumber()




        

        
