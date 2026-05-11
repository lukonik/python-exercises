import csv


def process_salaries():
    with open("45.csv") as file:
        csv_file = csv.reader(file)
        salary = 0
        next(csv_file)
        for _, row_salary in csv_file:
            salary += int(row_salary)
        print(
            f"Includes the original data and a final row: {salary / (csv_file.line_num - 1)}"
        )


process_salaries()