from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_ingredients(self) -> str:
        pass


class SimpleCoffee(Coffee):
    def get_cost(self) -> float:
        return 2.0

    def get_ingredients(self) -> str:
        return "Coffee"


class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee: Coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self) -> float:
        return self.decorated_coffee.get_cost()

    def get_ingredients(self) -> str:
        return self.decorated_coffee.get_ingredients()


class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return super().get_cost() + 0.5

    def get_ingredients(self) -> str:
        return super().get_ingredients() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return super().get_cost() + 0.2

    def get_ingredients(self) -> str:
        return super().get_ingredients() + ", Sugar"


if __name__ == "__main__":
    simple_coffee = SimpleCoffee()
    print(
        f"Cost: {simple_coffee.get_cost()}; Ingredients: {simple_coffee.get_ingredients()}"
    )

    milk_coffee = MilkDecorator(simple_coffee)
    print(
        f"Cost: {milk_coffee.get_cost()}; Ingredients: {milk_coffee.get_ingredients()}"
    )

    sugar_milk_coffee = SugarDecorator(milk_coffee)
    print(
        f"Cost: {sugar_milk_coffee.get_cost()}; Ingredients: {sugar_milk_coffee.get_ingredients()}"
    )
