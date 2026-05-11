class Pizza:
    marg = "MARRRG"

    def __init__(self, price: int):
        self.price = price

    @staticmethod
    def validate_topping(topping: str):
        if topping == "pineapple":
            return False
        return True

    @classmethod
    def margherita(cls):
        return cls(1000)


my_pizza = Pizza.margherita()
is_valid = Pizza.validate_topping("pineapple")

print(my_pizza)
print(is_valid)
