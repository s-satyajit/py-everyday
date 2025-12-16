class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__ (self):
        return f"{self.year} {self.brand} {self.model}"
        
    
car1 = Car("BMW", "X7", 2024)


