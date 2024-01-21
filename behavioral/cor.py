"""Chain of Responsibility.

The chain of responsibility pattern is a behavioral design pattern that allows
you to pass requests along a chanin of handlers. Instead of sending a request to
a specific handler, you send it to a chain of handlers. The request travels along
the chain until one of the handlers handles it.
"""

from typing import Protocol


class Handler(Protocol):
    def set_next(self, handler: "Handler") -> "Handler":
        ...

    def handle(self, request: int) -> str | None:
        ...


class AbstractHandler:
    _next_hanlder: Handler | None = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: int) -> str | None:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class ConcreteHandler1(AbstractHandler):
    def handle(self, request: int) -> str | None:
        if request < 10:
            return f"Handler 1: {request}"
        return super().handle(request)


class ConcreteHandler2(AbstractHandler):
    def handle(self, request: int) -> str | None:
        if 10 <= request < 20:
            return f"Handler 2: {request}"
        return super().handle(request)


class DefaultHandler(AbstractHandler):
    def handle(self, request: int) -> str:
        return f"DefaultHandler: No handler could process {request}"


if __name__ == "__main__":
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    default_handler = DefaultHandler()
    handler1.set_next(handler2).set_next(default_handler)
    for i in range(25):
        result = handler1.handle(i)
        if result:
            print(result)
