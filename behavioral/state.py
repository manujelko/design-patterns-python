"""State pattern.

The state design pattern is a behavioral design pattern that allows an object to alter
its behavior when its internal state changes. This pattern is particularly useful for
implementing state machines.
"""

from typing import Protocol


class State(Protocol):
    def publish(self) -> None:
        ...

    def review(self) -> None:
        ...


class Document:
    def __init__(self) -> None:
        self.state: State = Draft(self)

    def set_state(self, state: State) -> None:
        self.state = state

    def publish(self) -> None:
        self.state.publish()

    def review(self) -> None:
        self.state.review()


class Draft:
    def __init__(self, document: Document) -> None:
        self.document = document

    def publish(self) -> None:
        print("Moderation approved. Document is now published")
        self.document.set_state(Published(self.document))

    def review(self) -> None:
        print("Moderation is under review.")


class Published:
    def __init__(self, document: Document) -> None:
        self.document = document

    def publish(self) -> None:
        print("Document is already published")

    def review(self) -> None:
        print("Published document cannot be reviewed")


if __name__ == "__main__":
    document = Document()
    document.review()
    document.publish()
    document.review()
    document.publish()
