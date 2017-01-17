
# In python, it is possible to make class method appears as if they are class attributes

# this is 2nd  way to do with: using the property decorators.


class Complex1:

    def __init__(self, real=0, img=0):
        self._real = real   
        self._img = img

    def __str__(self):

        if self.img < 0:
            return "{} - {}j".format(self.real, abs(self.img))
        else:
            return "{} + {}j".format(self.real, self.img)    

    @property    
    def real(self):
        print("real getter called")
        return self._real
    
    @real.setter
    def real(self, real):
        print("real setter called with {}".format(real))

        # By intercepting setter, we can implment checks on the argument.
        if not (isinstance(real, int) or isinstance(real,float)):
            raise Exception("Argument not numeric")    
        self._real = real        

        
    @real.deleter
    def real(self):
        print("real deleter called.")            
        pass


        
    
    @property        
    def img(self):
        print("img getter called")        
        return self._img

    @img.setter    
    def img(self, img):
        print("img setter called with {}".format(img))

        # checking argument is of right type before setting it.
        if not (isinstance(img, int) or isinstance(img,float)):
            raise Exception("Argument not numeric")
        self._img = img

        
    @img.deleter        
    def img(self):
        print("img deleter called.")
        pass

  


def main():
    
    print("Testing Complex1")
    i1 = Complex1(1,2)

    print(i1)
    print(i1.real)
    print(i1.img)

    i1.real = 10
    i1.img = -10

    print(i1)
  
