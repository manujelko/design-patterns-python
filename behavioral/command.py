"""Command pattern.

The command pattern is a behavioral design pattern that turns a request into a
stand-alnone object containing all information about the request. The transformation
lets you parametrize methods with different requests, delay or queue a request's
execution, and support undoable operations.
"""

from typing import Protocol


class Command(Protocol):
    def execute(self) -> None:
        ...


class TextEditor:
    def __init__(self) -> None:
        self.text = ""

    def write(self, text: str) -> None:
        self.text += text

    def copy(self) -> str:
        return self.text

    def paste(self, clipboard: str) -> None:
        self.write(clipboard)


class CopyCommand:
    def __init__(self, editor: TextEditor) -> None:
        self.editor = editor
        self.clipboard: str = ""

    def execute(self) -> None:
        self.clipboard = self.editor.copy()


class PasteCommand:
    def __init__(self, editor: TextEditor, clipboard: str) -> None:
        self.editor = editor
        self.clipboard = clipboard

    def execute(self) -> None:
        self.editor.paste(self.clipboard)


class ShortcutKeys:
    def __init__(self) -> None:
        self.commands: list[Command] = []

    def add_command(self, command: Command) -> None:
        self.commands.append(command)

    def execute_commands(self) -> None:
        for command in self.commands:
            command.execute()


if __name__ == "__main__":
    editor = TextEditor()
    editor.write("Hello, ")
    copy_cmd = CopyCommand(editor)
    paste_cmd = PasteCommand(editor, "World!")
    shortcuts = ShortcutKeys()
    shortcuts.add_command(copy_cmd)
    shortcuts.add_command(paste_cmd)
    shortcuts.execute_commands()
    print(editor.text)
