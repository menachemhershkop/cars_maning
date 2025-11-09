from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_plate,year):
        self.__license_plate=license_plate
        self.__year=year
    def get_license(self):
        if self.__license_plate:
            return self.__license_plate
    def get_year(self):
        if self.__year:
            return self.__year
    def set_licence(self,new_license):
        if new_license:
            self.__license_plate=new_license
    def set_year(self,new_year):
        if new_year:
            self.__year=new_year
    @abstractmethod
    def calculate_annual_tax(self):
        pass