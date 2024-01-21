"""Prototype pattern.

The prototype pattern is used to create duplicate objects while keeping performance
in mind. This pattern involves creating a new object by copying an existing object,
known as the prototype. It's particularly useful when the construction of a new
instance is more efficient by copying an existing instance than by creating a new
one from scratch.
"""


import copy
from typing import Any


class Prototype:
    def clone(self) -> Any:
        pass


class Car(Prototype):
    def __init__(self, make: str, model: str, color: str):
        self.make = make
        self.model = model
        self.color = color

    def __str__(self) -> str:
        return f"{self.color} {self.make} {self.model}"

    def clone(self) -> "Car":
        return copy.deepcopy(self)


if __name__ == "__main__":
    original_car = Car("Tesla", "Model S", "Red")
    print(f"Original: {original_car}")

    cloned_car = original_car.clone()
    cloned_car.color = "Blue"
    print(f"Cloned: {cloned_car}")
