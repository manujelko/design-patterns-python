"""Memento pattern.

The memento pattern is a behavioral design patter that lets you save and restore the
previous state of an object without revealing the details of its implementation. This
pattern is useful for features like undo mechanisms in applications.
"""


class Memento:
    def __init__(self, state: str) -> None:
        self._state = state

    def get_saved_state(self) -> str:
        return self._state


class Originator:
    def __init__(self) -> None:
        self._state = ""

    def set_state(self, state: str) -> None:
        self._state = state

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_saved_state()

    def get_state(self) -> str:
        return self._state


class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._originator = originator
        self._mementos: list[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not self._mementos:
            return
        memento = self._mementos.pop()
        self._originator.restore(memento)


if __name__ == "__main__":
    editor = Originator()
    caretaker = Caretaker(editor)
    editor.set_state("State 1")
    caretaker.backup()
    editor.set_state("State 2")
    caretaker.backup()
    editor.set_state("State 3")
    print("Current state:", editor.get_state())
    caretaker.undo()
    print("After undo:", editor.get_state())
    caretaker.undo()
    print("After another undo:", editor.get_state())
