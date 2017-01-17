


class ImaginaryNum1:

    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img

    def __str__(self):

        if self.img < 0:
            return "{} - {}j".format(self.real, abs(self.img))
        else:
            return "{} + {}j".format(self.real, self.img)    

    def __get_real(self):
        return self.real

    def __get_img(self):
        return self.im

    def __set_real(self, real):
        self.real = real
        

    def __set_img(self, img):
        self.img


    
    name = property(__get_real, __get_img)






def main():
    print("Start")

    i1 = ImaginaryNum1(1,2)

    print(i1)
    print(i1.real)
    print(i1.img)

    i1.real = 10
    i1.img = -10

    print(i1)
  
