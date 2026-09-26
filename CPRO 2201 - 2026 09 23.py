
class Car:
    total_cars = 0
    
    def __init__(self, color, miles):
        self.color = color
        self.miles = miles
        Car.total_cars += 1
        
    def drive(self, miles):
        self.miles += miles # var = var + miles
        print(f"Driven {miles} - Total: {self.miles}")
        
    @classmethod
    def car_count(cls):
        print(f"Total cars: {cls.total_cars}")
        
Car.car_count()

c1 = Car("red", 10000)
c1.drive(50)
c1.car_count()
        
#c2 = Car("blue", 5000)
#c2.drive(100)

#c2.car_count()

#%%

class MathUtils:
    @staticmethod
    def add(n1, n2):
        return n1 + n2
        
res = MathUtils.add(2, 3)
print(f"res: {res}")

#%%







