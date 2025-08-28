class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNum(self):
        print(self.real,'i +',self.img,'j')

    def __add__(self,complex2):
        newReal=self.real+complex2.real
        newImg=self.img+complex2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,complex1):
        newReal=self.real-complex1.real
        newImg=self.img-complex1.img
        return Complex(newReal,newImg)

complex1=Complex(1,2)
complex1.showNum()

complex2=Complex(10,13)
complex2.showNum()

complex3=complex2-complex1
complex3.showNum()