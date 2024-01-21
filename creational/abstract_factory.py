"""Abstract Factory design pattern.

The abstract factory design pattern provides an interface for creating families of
related or dependent objects without specifying their concrete classes. It involves
multiple factory methods, one of each type of object to be created.
"""


from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def drive(self) -> str:
        pass


class Bike(ABC):
    @abstractmethod
    def ride(self) -> str:
        pass


class ElectricCar(Car):
    def drive(self) -> str:
        return "Driving an electric car"


class GasolineCar(Car):
    def drive(self) -> str:
        return "Driving a gasoline car"


class ElectricBike(Bike):
    def ride(self) -> str:
        return "Riding an electric bike"


class GasolineBike(Bike):
    def ride(self) -> str:
        return "Riding a gasoline bike"


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass

    @abstractmethod
    def create_bike(self) -> Bike:
        pass


class ElectricVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return ElectricCar()

    def create_bike(self) -> Bike:
        return ElectricBike()


class GasolineVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return GasolineCar()

    def create_bike(self) -> Bike:
        return GasolineBike()


if __name__ == "__main__":
    electric_factory = ElectricVehicleFactory()
    gasoline_factory = GasolineVehicleFactory()
    car = electric_factory.create_car()
    print(car.drive())
    bike = gasoline_factory.create_bike()
    print(bike.ride())
