class Flyer:
    def fly(self):
        print("Flying High!")


class Swimmer:
    def swim(self):
        print("Swimming fast!")


class Duck(Flyer, Swimmer):
    pass


d = Duck()
d.fly()
d.swim()
print(Duck.mro())