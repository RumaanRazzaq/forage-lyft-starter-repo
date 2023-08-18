import battery
from datetime import date, datetime

class NubbinBattery(battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self) -> bool:
        delta = self.__current_date - self.__last_service_date
        days = delta.days
        total_days = 1460
        for year in range(self.last_service_date.year, self.current_date.year + 1):
            if (year % 400 == 0) and (year % 100 == 0):
                total_days += 1
            elif (year % 4 ==0) and (year % 100 != 0):
                total_days += 1
        if days >= total_days:
            return True
        return False