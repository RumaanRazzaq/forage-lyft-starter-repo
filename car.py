import serviceable, engine, battery

class Car(serviceable):
    def __init__(self, engine: engine, battery: battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        if self.battery.needs_service() or self.engine.needs_service():
            return True
        return False