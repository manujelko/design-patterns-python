"""Iterator pattern.

The iterator pattern is a design pattern that allows sequential traversal through
a complex data structure without exposing its internal details. This pattern is
commonly used in Python to build iterators that can be used in for-loops and other
constructs that expect an iterable object.
"""

from collections.abc import Iterator
from typing import Protocol


class Book:
    def __init__(self, title: str) -> None:
        self.title = title

    def __str__(self) -> str:
        return self.title


class Iterable(Protocol):
    def __iter__(self) -> Iterator[Book]:
        ...


class BookCollection:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def __iter__(self) -> Iterator[Book]:
        return BookIterator(self.books)


class BookIterator(Iterator[Book]):
    def __init__(self, books: list[Book]) -> None:
        self._books = books
        self._index = 0

    def __next__(self) -> Book:
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration()


if __name__ == "__main__":
    book_collection = BookCollection()
    book_collection.add_book(Book("1984"))
    book_collection.add_book(Book("To Kill a Mockingbird"))
    book_collection.add_book(Book("The Great Gatsby"))
    for book in book_collection:
        print(book)
