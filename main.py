from cars.car import Car
from cars.electric_car import ElectricCar
from cars.truck import Truck

car = Car(819501,2003)
truck=Truck(15349,2020,150)
electric_car=ElectricCar(983462,2025)
car_list=[car,truck,electric_car]
for i in car_list:
    print(i.calculate_annual_tax())
car.set_year(2008)
print(car.get_year())
electric_car.charge()