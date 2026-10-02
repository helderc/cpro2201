
class MyClass:
    def __init__(self, x, y, z):
        # public
        self.x = x
        # protected
        self._y = y
        # privated
        self.__z = z
        
    def get_z(self):
        return self.__z
    
    def set_z(self, z):
        # LNL-NLN
        # 001-ZW8
        self.__z = z

        
obj1 = MyClass(2, 3, 4)

# name mangling
print(obj1._MyClass__z)

obj1._MyClass__z = 123
print(obj1.get_z())


#%%

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):        
        ...    

class Square(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 2 * 3.14 * self.r**2
    
# Rectangle, Circle, ...


sq1 = Square(2, 4)
#print(f"sq1: {sq1.area()}")
circ1 = Circle(5)
#print(f"circ1: {circ1.area()}")

#shp = Shape()
#shp.area()

def calcAllAreas(shape_list:list):
    for s in shape_list:
        print(s.area())

l = [sq1, circ1]
calcAllAreas(l)
























