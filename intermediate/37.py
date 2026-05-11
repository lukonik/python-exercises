class Student:
    def __init__(self, name: str):
        self.name = name
        self.__score = 0

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value: int):
        if 0 < value < 100:
            self.__score = value
        else:
            raise ValueError(
                f"Score value must be between 0 and 100, currently it is: {value}"
            )


s = Student("Kevin")
s.score = 90  # Should trigger a ValueError
print(s.score)
