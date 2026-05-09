class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand

    def fuel_type():
        pass


class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electricity"


car = ElectricCar("Tesla")

print(car.brand)
print(car.fuel_type())