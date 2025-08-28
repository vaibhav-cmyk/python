import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def Area(self):
        area=math.pi*self.radius*self.radius
        print('area is:',area)

    def permeter(self):
        perimeter=2* (math.pi) *self.radius
        print('perimeter is:',perimeter)

c1=Circle(21)
c1.Area()
c1.permeter()