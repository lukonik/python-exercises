from datetime import datetime
from dateutil.relativedelta import relativedelta


def countdown_to_new_year():
    current_date = datetime.now()
    new_year = current_date + relativedelta(day=31, month=12)
    result =new_year - current_date
    print(result)


countdown_to_new_year()
