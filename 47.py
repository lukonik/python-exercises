import re

compiled=re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")

def extract_emails(text: str):
    emails = compiled.findall(text)
    return emails


text = "Contact us at support@company.com or sales.dept@office.org for help."


print(extract_emails(text))
