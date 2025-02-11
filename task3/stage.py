import datetime
from exception import InvalidDateFormatException
from utils import check_date_format

class Stage:
    def __init__(self, cost, start_date, end_date, description, status="запланирован"):
        try:
            self.cost = cost
            self.start_date = check_date_format(start_date)
            self.end_date = check_date_format(end_date)
            self.description = description
            self.status = status
        except InvalidDateFormatException:
            raise InvalidDateFormatException("Неверный формат даты. Используйте формат дд.мм.гггг.")
        
    def next(self):
        pass

    def prev(self):
        pass

    def start(self):
        self.status = "осуществляется"

    def stop(self):
        self.status = "выполнен"

    def reject(self):
        self.status = "забракован"

class Project(Stage):
    pass

class Foundation(Stage):
    pass

class Walls(Stage):
    pass

class Roof(Stage):
    pass

class WindowsInstallation(Stage):
    pass

class Finishing(Stage):
    pass