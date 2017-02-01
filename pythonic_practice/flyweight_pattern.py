
# The flyweight pattern is a memory optimization pattern
# The ideas is to ensure the object sharing the same state can use the same memory
# for that shared state. This pattern can save a lot of memory when there is a huge number of the
# shared state.


# Similar to the singleton pattern, one way to implement this is to make use of the __new__
# class method.



# this implementation use weakref to ensure the key in the _models dict gets removed when
# del is called on the object reference.
# see https://docs.python.org/3/library/weakref.html

import weakref

class HandphoneModel:

    #_models = {}  # this won't work.
    _models = weakref.WeakValueDictionary()

    def __new__(cls, model_name, *args, **kwargs):

        model = cls._models.get(model_name)
        if not model:
            print("New obj created for {}".format(model_name))
            model = super().__new__(cls)
            cls._models[model_name] = model
        return model


    def __del__(self):
        print("__del__ called for {}".format(self.model))

        

    def __init__(self, model_name):
        if not hasattr(self, "initted"):
            self.model = model_name
            self.initted = True



            
def test():
    
    print("Start")

    h1 = HandphoneModel("iphone7_white")
    h2 = HandphoneModel("iphone6_black")
    h3 = HandphoneModel("iphone7_white")  # this should not result in a new object

    del h2

    print(HandphoneModel._models)



 
