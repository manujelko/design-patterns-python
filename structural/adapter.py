"""Adapter pattern.

The adapter pattern is a structural design pattern that allows objects with
incompatible interfaces to work together. It involves a wrapper (the adapter) which
makes one existing class (the adaptee) compatible with another interface (the target).
"""


class EuropeanSocket:
    def charge(self) -> str:
        return "Charging with European socket"


class USASocket:
    def power(self) -> str:
        return "Powering with USA socket"


class SocketAdapter(EuropeanSocket):
    def __init__(self, usa_socket: USASocket) -> None:
        self.usa_socket = usa_socket

    def charge(self) -> str:
        power = self.usa_socket.power()
        return f"Adapting {power} to European charging standard"


if __name__ == "__main__":
    usa_socket = USASocket()
    adapter = SocketAdapter(usa_socket)
    print(adapter.charge())
