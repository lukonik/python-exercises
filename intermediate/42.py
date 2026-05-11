class CPU:
    def __init__(self, model: str):
        self.model = model


class RAM:
    def __init__(self, size: int):
        self.size = size


class Computer:
    def __init__(self, model: str, size: int):
        self.cpu = CPU(model)
        self.ram = RAM(size)

    def __repr__(self):
        return f"Computer with {self.cpu.model} and {self.ram.size}G RAM"


my_comp = Computer("Intel I7", 16)

print(my_comp)
