"""Builder pattern.

The builder pattern is a creational design pattern that lets you construct complex
objects step by step. This pattern is useful when an object must be created with
many possible configurations and is composed of numerous parts or components.
"""


from abc import ABC, abstractmethod


class House:
    def __init__(self):
        self.foundation = ""
        self.structure = ""
        self.roof = ""
        self.interior = ""

    def __str__(self) -> str:
        return (
            f"House with {self.foundation} foundation "
            f"{self.structure} structure "
            f"{self.roof} roof "
            f"and {self.interior} interior"
        )


class HouseBuilder(ABC):
    @abstractmethod
    def build_foundation(self) -> None:
        pass

    @abstractmethod
    def build_structure(self) -> None:
        pass

    @abstractmethod
    def build_roof(self) -> None:
        pass

    @abstractmethod
    def build_interior(self) -> None:
        pass

    @abstractmethod
    def get_result(self) -> House:
        pass


class StoneHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self) -> None:
        self.house.foundation = "stone"

    def build_structure(self) -> None:
        self.house.structure = "stone walls"

    def build_roof(self) -> None:
        self.house.roof = "slate"

    def build_interior(self) -> None:
        self.house.interior = "stone and wood"

    def get_result(self) -> House:
        return self.house


class WoodHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self) -> None:
        self.house.foundation = "wood"

    def build_structure(self) -> None:
        self.house.structure = "wooden beams"

    def build_roof(self) -> None:
        self.house.roof = "wooden shingles"

    def build_interior(self) -> None:
        self.house.interior = "wood panels"

    def get_result(self) -> House:
        return self.house


class ConstructionEngineer:
    """Director."""

    def __init__(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_foundation()
        self.builder.build_structure()
        self.builder.build_roof()
        self.builder.build_interior()

    def get_house(self) -> House:
        return self.builder.get_result()


if __name__ == "__main__":
    stone_builder = StoneHouseBuilder()
    engineer = ConstructionEngineer(stone_builder)
    engineer.construct_house()
    house = engineer.get_house()
    print(house)

    wood_builder = WoodHouseBuilder()
    engineer = ConstructionEngineer(wood_builder)
    engineer.construct_house()
    house = engineer.get_house()
    print(house)
