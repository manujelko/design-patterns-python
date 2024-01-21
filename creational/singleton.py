"""Singleton pattern.

The singleton pattern ensures that a class has only one instance and provides a gobal
point of access to it. This pattern is often used for managing shared resources,
like database connections or configurations.
"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(f"s1 is s2: {s1 is s2}")
