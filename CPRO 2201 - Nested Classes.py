class Company:
    class Address:
        def __init__(self, city, province):
            self.city = city
            self.province = province

        def __str__(self):
            return f"{self.city}, {self.province}"

    def __init__(self, name, city, province):
        self.name = name
        self.address = Company.Address(city, province)

    def describe(self):
        print(f"{self.name} - {self.address}")


company = Company("Red Deer Polytechnic", "Red Deer", "Alberta")

company.describe()