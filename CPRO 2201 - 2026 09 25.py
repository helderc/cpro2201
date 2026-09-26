
class Car:
    def __init__(self, maker, color=None, mileage=0):
        print("Constructor called!")        
        self.color = "No color" if not color else color
        self.mileage = mileage
        self.maker = maker
        
#print("string1", "string2", sep="@")

car1 = Car("", 5000)
print(f"Car: {car1.color}, Mileage: {car1.mileage}\n")

car2 = Car("green")
print(f"Car: {car2.color}, Mileage: {car2.mileage}")
print(car2.maker, "\n")

car3 = Car("Toyota")
print(f"Car: {car3.color}, Mileage: {car3.mileage}\n")

car4 = Car(mileage=1000, color="yellow", maker="Nissan")
print(f"Car: {car4.color}, Mileage: {car4.mileage}\n")

#%%


class Car:
    def __init__(self, maker, color=None, mileage=0):
        print("Constructor called!")        
        self.color = "No color" if not color else color
        self.mileage = mileage
        self.maker = maker
        
    def __del__(self):
        print("Destructor called!")
        

car4 = Car(mileage=1000, color="yellow", maker="Nissan")
print(f"Car: {car4.color}, Mileage: {car4.mileage}\n")

del car4

#%%

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
    
    def get_y(self):
        return self._y

        
obj1 = MyClass(2, 3, 4)
print(obj1.x)
print(obj1._y)
#print(obj1.__z)
print(obj1.get_z())

obj1.x = 10
obj1._y = 15
obj1.__z = 1111

print(obj1.__z)
print(obj1.get_z())

print(obj1.x)
print(obj1._y, obj1.get_y())













