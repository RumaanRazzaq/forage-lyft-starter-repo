import engine

class SternmanEngine(engine):
    def __init__(self, warning_light_is_on):
        self.__warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        if self.__warning_light_is_on:
            return True
        return False
