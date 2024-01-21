from typing import Protocol


class TextFormatter(Protocol):
    def format(self, text: str) -> str:
        ...


class UpperCaseFormatter:
    def format(self, text: str) -> str:
        return text.upper()


class LowerCaseFormatter:
    def format(self, text: str) -> str:
        return text.lower()


class TextEditor:
    def __init__(self, formatter: TextFormatter) -> None:
        self.formatter = formatter

    def set_formatter(self, formatter: TextFormatter) -> None:
        self.formatter = formatter

    def format_text(self, text: str) -> str:
        return self.formatter.format(text)


if __name__ == "__main__":
    upper_case_formatter = UpperCaseFormatter()
    lower_case_formatter = LowerCaseFormatter()
    editor = TextEditor(upper_case_formatter)
    print(editor.format_text("Hello, World!"))
    editor.set_formatter(lower_case_formatter)
    print(editor.format_text("Hello, World!"))
