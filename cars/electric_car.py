from cars.car import Car
from mixins.electric import ElectricMixin


class ElectricCar(Car, ElectricMixin):
    def calculate_annual_tax(self):
        return 250