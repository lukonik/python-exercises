class PowerOfTwo:
    def __init__(self, max: int):
        self.max = max
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.max:
            raise StopIteration()
        output = 2**self.index
        self.index += 1
        return output


powers = PowerOfTwo(4)

for p in powers:
    print(p)
