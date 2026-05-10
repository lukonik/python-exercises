from typing import Any

students: dict = {}


def add_student(key: int, name: str, grade: str):
    students[key] = {"name": name, "grade": grade}


def update_grade(key: int, grade: str):
    if key in students:
        students[key]["grade"] = grade


def display_all():
    print(students)


add_student(101, "Alice", "A")
update_grade(101, "A+")
add_student(102, "Bob", "B")
display_all()
