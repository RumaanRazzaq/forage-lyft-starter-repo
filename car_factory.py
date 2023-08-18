from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tyres.carrigan_tyres import CarriganTyres
from tyres.octoprime_tyres import OctoprimeTyres
from car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage: int, last_service_mileage: int): 
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tyres = CarriganTyres([0.1, 0.2, 0.3, 0.4])
        car = Car(engine, battery, tyres)
        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage: int, last_service_mileage: int): 
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tyres = CarriganTyres([0.1, 0.2, 0.3, 0.4])
        car = Car(engine, battery, tyres)
        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on: bool): 
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tyres = OctoprimeTyres([0.1, 0.2, 0.3, 0.4])
        car = Car(engine, battery, tyres)
        return car
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage: int, last_service_mileage: int): 
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tyres = CarriganTyres([0.1, 0.2, 0.3, 0.4])
        car = Car(engine, battery, tyres)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage: int, last_service_mileage: int): 
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tyres = OctoprimeTyres([0.1, 0.2, 0.3, 0.4])
        car = Car(engine, battery, tyres)
        return car
    
