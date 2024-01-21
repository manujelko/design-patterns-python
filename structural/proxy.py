"""Proxy pattern.

The proxy pattern is a structural design pattern that provides a surrogate or
placeholder for another object to control access to it. This pattern is useful when
you want to add a layer of indirection to an object, for example, to add extra
functionality like access control, lazy initialization, logging etc., without
changing the object's code.
"""

from typing import Protocol


class Book(Protocol):
    def display_content(self) -> None:
        ...


class RealBook:
    def __init__(self, content: str) -> None:
        self.content = content

    def display_content(self) -> None:
        self.read_book = real_book


class BookProxy:
    def __init__(self, real_book: RealBook) -> None:
        self.read_book = real_book
        self.access_count = 0

    def display_content(self) -> None:
        self.access_count += 1
        print(f"Displaying content for the {self.access_count} time(s).")
        self.read_book.display_content()


if __name__ == "__main__":
    real_book = RealBook("The contents of the book.")
    proxy_book = BookProxy(real_book)
    proxy_book.display_content()
    proxy_book.display_content()
