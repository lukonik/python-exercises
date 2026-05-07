from dateutil.parser import parse
from datetime import datetime


def age_calculator():
    date_prompt = input("Enter date with format: YYYY-MM-DD ")
    parsed_date = parse(date_prompt)
    now = datetime.now()
    diff = now - parsed_date
    print(f"Days: {diff.days}")


age_calculator()
