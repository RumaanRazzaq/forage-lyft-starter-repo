from tyres.tyres import Tyres

class OctoprimeTyres(Tyres):
    def __init__(self, tyre_wear):
        self.__tyre_wear = tyre_wear

    def needs_service(self) -> bool:
        return sum(self.__tyre_wear) >= 3