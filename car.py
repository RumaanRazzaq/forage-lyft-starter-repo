from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        if self.battery.needs_service() or self.engine.needs_service():
            return True
        return False