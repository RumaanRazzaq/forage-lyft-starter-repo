from battery.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self) -> bool:
        result = self.__last_service_date.replace(year=self.__last_service_date.year + 2)
        if result < self.__current_date:
            return True
        else:
            return False