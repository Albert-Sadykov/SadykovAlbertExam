from stage import Stage
from exception import InvalidDateFormatException

class TestDateFormat:
    @staticmethod
    def run_tests():
        try:
            Stage(1000, "01-01-2025", "10.01.2025", "Неверная дата")
        except InvalidDateFormatException as e:
            print(e)
        
        try:
            Stage(1000, "01.01.2025", "10-01-2025", "Неверная дата")
        except InvalidDateFormatException as e:
            print(e)

if __name__ == "__main__":
    TestDateFormat.run_tests()