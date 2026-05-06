from dataclasses import dataclass


@dataclass
class Car:
    make: str
    model: str
    year: int

    def start_engine(self):
        print(f"Make:{self.make}, Model:{self.model}, Year:{self.year}")


car = Car("Toyota", "Prius", 2024)

car.start_engine()