import re
from exception import InvalidDateFormatException

def check_date_format(date_string):
    if date_string[2] != '.' or date_string[5] != '.' or len(date_string) != 10:
        raise InvalidDateFormatException()
    
    day = date_string[:2]
    month = date_string[3:5]
    year = date_string[6:]

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        raise InvalidDateFormatException()
    
    day = int(day)
    month = int(month)

    if month < 1 or month > 12:
        raise InvalidDateFormatException()
    
    if day < 1 or day > 31:
        raise InvalidDateFormatException()
    
    return date_string




    