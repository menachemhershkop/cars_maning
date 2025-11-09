from classes.engine import Engine
from classes.vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, license_plate,year,max_load):
        super().__init__(license_plate,year)
        self.engine=Engine(15000,"soler")
        self.max_load=max_load
    def calculate_annual_tax(self):
        return self.engine.horsepower * (self.max_load/2)