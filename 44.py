from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int


b1 = Book("1984", "George Orwell", 350)

print(b1)
