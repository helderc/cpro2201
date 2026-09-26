class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

emp = Employee("Benny", 10000)

print(f"{emp.name}'s salary is {emp.get_salary()}")
emp.set_salary(5000)
print(f"{emp.name}'s salary is {emp.get_salary()}")