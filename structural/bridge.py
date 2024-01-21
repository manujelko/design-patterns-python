"""Bridge pattern.

The bridge pattern is a structural design pattern that decouples an abstraction
from its implementation so that the two can vary independently. It's especially
useful when both the abstraction and its implementation can have different hierarchies.
"""

from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    @abstractmethod
    def is_on(self) -> bool:
        pass


class Radio(Device):
    def __init__(self):
        self._on = False

    def turn_on(self) -> None:
        self._on = True
        print("Radio turned on")

    def turn_off(self) -> None:
        self._on = False
        print("Radio turned off")

    def is_on(self) -> bool:
        return self._on


class TV(Device):
    def __init__(self):
        self._on = False

    def turn_on(self) -> None:
        self._on = True
        print("TV turned on")

    def turn_off(self) -> None:
        self._on = False
        print("TV turned off")

    def is_on(self) -> bool:
        return self._on


class RemoteControl:
    def __init__(self, device: Device) -> None:
        self.device = device

    def toggle_power(self) -> None:
        if self.device.is_on():
            self.device.turn_off()
        else:
            self.device.turn_on()


class AdvancedRemoteControl(RemoteControl):
    def mute(self) -> None:
        print("Device muted")


if __name__ == "__main__":
    tv = TV()
    remote = RemoteControl(tv)
    remote.toggle_power()
    remote.toggle_power()
    radio = Radio()
    advanced_remote = AdvancedRemoteControl(radio)
    advanced_remote.toggle_power()
    advanced_remote.mute()
