
from math import hypot


class Complex:

    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img

    def __repr__(self):
        return '{}i + {}j'.format(self.real, self.img)

    def __abs__(self):
        return  hypot(self.real, self.img)

    def __add__(self,other):
        real = self.real + other.real
        img  = self.img + other.img        
        return Complex(real, img)
