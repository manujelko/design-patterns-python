"""Composite pattern.

The composite pattern is a structural design pattern that allows you to compose
objects into tree structures to represent part-whole hierarchies. This pattern lets
clients treat individual objects and composition of object uniformly.
"""


from abc import ABC, abstractmethod


class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self) -> None:
        pass


class File(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name

    def show_details(self) -> None:
        print(f"File: {self.name}")


class Directory(FileSystemComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: list[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> None:
        self.children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        self.children.remove(component)

    def show_details(self) -> None:
        print(f"Directory: {self.name}")
        for child in self.children:
            child.show_details()


if __name__ == "__main__":
    root = Directory("root")
    dir1 = Directory("dir1")
    dir2 = Directory("dir2")
    file1 = File("file1")
    file2 = File("file2")
    file3 = File("file3")
    dir1.add(file1)
    dir2.add(file2)
    dir2.add(file3)
    root.add(dir1)
    root.add(dir2)
    root.show_details()
