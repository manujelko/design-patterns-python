"""Factory design pattern.

The Factory pattern is a creational design pattern that provides an interface
for creating objects in a superclass, but allows subclasses to alter the type
of objects that will be created.
"""


from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self) -> str:
        pass


class Car(Vehicle):
    def drive(self) -> str:
        return "Driving a car"


class Truck(Vehicle):
    def drive(self) -> str:
        return "Driving a truck"


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Unknown vehicle type")


if __name__ == "__main__":
    vehicle_type = "car"
    vehicle = VehicleFactory.get_vehicle(vehicle_type)
    print(vehicle.drive())
