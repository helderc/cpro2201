class MyClass():
    def __init__(self, x, y, z):
        # public
        self.x = x
        # protected
        self._y = y
        # private
        self.__z = z


obj1 = MyClass(3, 4, 5)

print(obj1.x)
obj1.x = 50
print(obj1.x)

print(obj1._y)
obj1._y = 25
print(obj1._y)

# not accessible error
print(obj1.__z)