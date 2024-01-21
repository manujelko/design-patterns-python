"""Template Method pattern.

The template method pattern is a behavioral design pattern that defines the skeleton
of an algorithm in an operation, deferring some steps to subclasses. It lets one
redefine certain steps of an algorithm without changing the algorithm's structure.
"""

from abc import ABC, abstractmethod


class Recipe(ABC):
    def prepare_recipe(self) -> None:
        self.mix_ingredients()
        self.cook()
        self.serve()

    @abstractmethod
    def mix_ingredients(self) -> None:
        pass

    @abstractmethod
    def cook(self) -> None:
        pass

    def serve(self) -> None:
        print("Serving the dish.")


class CakeRecipe(Recipe):
    def mix_ingredients(self) -> None:
        print("Mixing flour, sugar, and eggs.")

    def cook(self) -> None:
        print("Baking the cake.")


class BreadRecipe(Recipe):
    def mix_ingredients(self) -> None:
        print("Mixing flour, yeast, and water.")

    def cook(self) -> None:
        print("Baking the bread")


if __name__ == "__main__":
    cake = CakeRecipe()
    cake.prepare_recipe()
    bread = BreadRecipe()
    bread.prepare_recipe()
