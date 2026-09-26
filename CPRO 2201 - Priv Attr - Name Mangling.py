class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

emp = Employee("Benny", 10000)

# AttributeError: 'Employee' object has no attribute '__salary'
#print(f"{emp.name}'s salary is {emp.__salary}")

# however...
print(f"{emp.name}'s salary is {emp._Employee__salary}")

emp._Employee__salary = 5000
print(f"{emp.name}'s salary is {emp._Employee__salary}")