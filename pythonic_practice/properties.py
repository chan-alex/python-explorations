
# In python, it is possible to make class method appears as if they are class attributes

# this is one way: using the "property" declaration.
# With this method it is important to name the actual data attribute and the getters/setters
# correctly or risk infinite recurision.
class Complex1:

    def __init__(self, real=0, img=0):
        self._real = real   
        self._img = img

    def __str__(self):

        if self.img < 0:
            return "{} - {}j".format(self.real, abs(self.img))
        else:
            return "{} + {}j".format(self.real, self.img)    

        
    def _get_real(self):
        print("_get_real called")
        return self._real
    

    def _set_real(self, real):
        print("_set_real called with {}".format(real))

        # By intercepting setter, we can implment checks on the argument.
        if not (isinstance(real, int) or isinstance(real,float)):
            raise Exception("Argument not numeric")    
        self._real = real        

        
    def _del_real(self):
        pass


    
    def _get_img(self):
        print("_get_img called")        
        return self._img

    
    def _set_img(self, img):
        print("_set_img called with {}".format(img))

        # checking argument is of right type before setting it.
        if not (isinstance(img, int) or isinstance(img,float)):
            raise Exception("Argument not numeric")
        self._img = img

        
    def _del_img(self):
        pass

    # to see docstring, use help(Complex1)
    real = property(_get_real, _set_real, _del_real, "Sets the real part") 
    img = property(_get_img, _set_img, _del_real, "Sets the imaginary")    

  


def main():
    
    print("Testing Complex1")
    i1 = Complex1(1,2)

    print(i1)
    print(i1.real)
    print(i1.img)

    i1.real = 10
    i1.img = -10

    print(i1)
  
