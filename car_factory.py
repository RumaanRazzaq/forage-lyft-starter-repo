from engine import capulet_engine, sternman_engine, willoughby_engine 
from battery import spindler_battery, nubbin_battery
import car
from datetime import date

class CarFactory:
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = spindler_battery(last_service_date, current_date)
        return car(engine, battery)

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = spindler_battery(last_service_date, current_date)
        return car(engine, battery)

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool): 
        engine = sternman_engine(warning_light_on)
        battery = spindler_battery(last_service_date, current_date)
        return car(engine, battery)
    
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
        engine = willoughby_engine(current_mileage, last_service_mileage)
        battery = nubbin_battery(last_service_date, current_date)
        return car(engine, battery)
    
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): 
        engine = capulet_engine(current_mileage, last_service_mileage)
        battery = nubbin_battery(last_service_date, current_date)
        return car(engine, battery)
    
if __name__ == "__main__":
    factory = CarFactory()
    car1 = factory.create_calliope("01/02/2003", 15000, 0)
    print(car1.needs_service())