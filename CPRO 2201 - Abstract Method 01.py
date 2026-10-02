class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    pass  # forgot area()

s = Square()  # no error...
s.area()      # ...fails here

