class TreeType:
    def __init__(self, name: str, color: str, texture: str) -> None:
        self.name = name
        self.color = color
        self.texture = texture

    def display(self, x: int, y: int, age: int) -> None:
        print(
            f"Tree type: {self.name}, Color: {self.color}, Texture: {self.texture}, "
            f"Position: ({x}, {y}), Age: {age} years"
        )


class TreeFactory:
    _tree_types: dict[str, TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        if not cls._tree_types.get(name):
            cls._tree_types[name] = TreeType(name, color, texture)
            print("Creating new TreeType")
        else:
            print("Reusing existing TreeType")
        return cls._tree_types[name]


class Tree:
    def __init__(self, x: int, y: int, age: int, tree_type: TreeType) -> None:
        self.x = x
        self.y = y
        self.age = age
        self.tree_type = tree_type

    def display(self) -> None:
        self.tree_type.display(self.x, self.y, self.age)


class Forest:
    def __init__(self) -> None:
        self.trees: tuple[Tree, ...] = ()

    def plant_tree(
        self, x: int, y: int, age: int, name: str, color: str, texture: str
    ) -> None:
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        tree = Tree(x, y, age, tree_type)
        self.trees += (tree,)

    def display_forest(self):
        for tree in self.trees:
            tree.display()


if __name__ == "__main__":
    forest = Forest()
    forest.plant_tree(1, 2, 5, "Oak", "Green", "Rough")
    forest.plant_tree(3, 4, 10, "Oak", "Green", "Rough")
    forest.plant_tree(5, 6, 15, "Birch", "White", "Smooth")
    forest.display_forest()
