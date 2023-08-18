from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery, tyres) -> None:
        self.engine = engine
        self.battery = battery
        self.tyres = tyres

    def needs_service(self) -> bool:
        if self.battery.needs_service() or self.engine.needs_service() or self.tyres.needs_service():
            return True
        return False