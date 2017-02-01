
# Simpleton is a pattern for ensuring only a single instance of a class exists.

# Genereally considered an anti pattern.in python.

# In most object orient language, simgletons are implement by make the constructor private so
# that it cannot be used to create new instane of the singleton and providing a static method
# that returns a reference to the single instance.
# The way to mimic this is to overrdide the __new__ class method.


class  Singleton:
    _singleton = None

    def __new__(c, *args, **kwargs):
        if not c._singleton:
            c._singleton = super(Singleton, c).__new__(c, *args, **kwargs)

        return c._singleton



def test():

    s1 = Singleton()
    s2 = Singleton()

    if s1 == s2:
        print("Same")
    else:
        print("Not same")
