from tyres.tyres import Tyres

class CarriganTyres(Tyres):
    def __init__(self, tyre_wear):
        self.__tyre_wear = tyre_wear
        
    def needs_service(self) -> bool:
        for tire in self.__tyre_wear:
            if tire >= 0.9:
                return True
        return False