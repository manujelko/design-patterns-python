"""Mediator pattern.

The mediator pattern is a behavioral design pattern that reduces coupling between
classes by moving their communication logic to a mediator class. This pattern is
especially useful when you have several objects interacting with each other, leading
to complex communication logic.
"""

from abc import ABC, abstractmethod


class Colleague(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def send_message(self, message: str) -> None:
        pass

    @abstractmethod
    def receive_message(self, sender_name: str, message: str) -> None:
        pass


class Mediator(ABC):
    @abstractmethod
    def register_colleague(self, colleague: Colleague) -> None:
        pass

    @abstractmethod
    def broadcast_message(self, sender: Colleague, message: str) -> None:
        pass


class ChatRoom(Mediator):
    def __init__(self) -> None:
        self.colleagues: list[Colleague] = []

    def register_colleague(self, colleague: Colleague) -> None:
        self.colleagues.append(colleague)

    def broadcast_message(self, sender: Colleague, message: str) -> None:
        for colleague in self.colleagues:
            if colleague != sender:
                colleague.receive_message(sender.get_name(), message)


class User(Colleague):
    def __init__(self, name: str, chat_room: ChatRoom) -> None:
        self.name = name
        self.chat_room = chat_room
        chat_room.register_colleague(self)

    def get_name(self) -> str:
        return self.name

    def send_message(self, message: str) -> None:
        print(f"{self.name} sends message: '{message}'")
        self.chat_room.broadcast_message(self, message)

    def receive_message(self, sender_name: str, message: str) -> None:
        print(f"{self.name} received a message from {sender_name}: '{message}'")


if __name__ == "__main__":
    chat_room = ChatRoom()
    alice = User("Alice", chat_room)
    bob = User("Bob", chat_room)
    charlie = User("Charlie", chat_room)
    alice.send_message("Hi there!")
    bob.send_message("Hey!")
    charlie.send_message("Hello everyone!")
