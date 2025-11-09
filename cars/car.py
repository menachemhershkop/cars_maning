from classes.engine import Engine
from classes.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, license_plate,year):
        super().__init__(license_plate,year)
        self.engine=Engine(None,None)

    def calculate_annual_tax(self):
        if self.get_year()>2020:
            return (self.engine.horsepower *0.2)*13
        if self.get_year() >2010:
            return (self.engine.horsepower *0.2)*10
        else:
            return (self.engine.horsepower*0.2)*5