"""Visitor pattern.

The visitor pattern is a behavioral pattern that allows adding new operations to
existing object structures without modifying them. This pattern is useful when
you have a complex object structure and want to perform operations on these objects
that don't necessarily fit into their class hierarchy.
"""

from abc import ABC, abstractmethod


class DocumentVisitor(ABC):
    @abstractmethod
    def visit_text_document(self, doc: "TextDocument") -> None:
        pass

    @abstractmethod
    def visit_pdf_document(self, doc: "PDFDocument") -> None:
        pass


class Document(ABC):
    @abstractmethod
    def accept(self, visitor: DocumentVisitor) -> None:
        pass


class TextDocument(Document):
    def accept(self, visitor: DocumentVisitor) -> None:
        visitor.visit_text_document(self)


class PDFDocument(Document):
    def accept(self, visitor: DocumentVisitor) -> None:
        visitor.visit_pdf_document(self)


class RenderVisitor(DocumentVisitor):
    def visit_text_document(self, doc: TextDocument) -> None:
        print("Rendering a text document")

    def visit_pdf_document(self, doc: PDFDocument) -> None:
        print("Rendering a PDF document")


class ExportVisitor(DocumentVisitor):
    def visit_text_document(self, doc: TextDocument) -> None:
        print("Exporting a text document")

    def visit_pdf_document(self, doc: PDFDocument) -> None:
        print("Exporting a PDF document")


if __name__ == "__main__":
    documents = [TextDocument(), PDFDocument()]
    render_visitor = RenderVisitor()
    export_visitor = ExportVisitor()
    for doc in documents:
        doc.accept(render_visitor)
        doc.accept(export_visitor)
