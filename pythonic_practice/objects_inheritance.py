
# All class inherts from the "object" class.
class class1(object):
    pass

# is same as:
class class1():
    pass

# This is an example of inheritence
class RealNum():    
    def __init__(self, r=0):
        self.real = r

class ImaginaryNum(RealNum):    
    def __init__(self, r=0, j=0):
        super().__init__(r)    # this initialize the base variables.
        self.imaginary = j

        

r1 = RealNum(10)
print(r1.real)

i1 = ImaginaryNum(10, 10)
print("{} + {}j ".format(i1.real, i1.imaginary))


