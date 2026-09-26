class Vehicle:
    def __init__(self, brand):
        self._brand = brand

    def describe(self):
        print(f"This is a {self._brand} vehicle.")


class Car(Vehicle):
    def show_brand(self):
        print(f"Car brand: {self._brand}")


car = Car("Toyota")

car.show_brand()       
car.describe()

# also works, but shouldn't be used --> getter/setter
print(car._brand)     