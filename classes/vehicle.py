from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_plate,year):
        self.__license_plate=license_plate
        self.__year=year
    def get_license(self):
        print(self.__license_plate)
    def get_year(self):
        print(self.__year)
    def set_licence(self,new_license):
        self.__license_plate=new_license
    def set_year(self,new_year):
        self.__year=new_year
    @abstractmethod
    def calculate_annual_tax(self):
        pass