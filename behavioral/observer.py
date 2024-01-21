"""Observer pattern.

The obserer pattern is a behavioral pattern that defines a one-to-many dependency
between objects. When one object changes state, all its dependents are notified and
updated automatically. This pattern is often used in implementing distributed event
handling systems.
"""

from typing import Protocol


class Observer(Protocol):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        ...


class Subject(Protocol):
    def attach(self, observer: Observer) -> None:
        pass

    def detach(self, observer: Observer) -> None:
        ...

    def notify(self) -> None:
        pass


class WeatherStation:
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(
        self, temperature: float, humidity: float, pressure: float
    ) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()


class TemperatureDisplay:
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"TemperatureDisplay: New temperature is {temperature}")


class HumidityDisplay:
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"HumidityDisplay: New humidity is {humidity}")


if __name__ == "__main__":
    weather_station = WeatherStation()
    temp_display = TemperatureDisplay()
    humidity_display = HumidityDisplay()
    weather_station.attach(temp_display)
    weather_station.attach(humidity_display)
    weather_station.set_measurements(25.4, 65, 1013.1)
    weather_station.set_measurements(22.3, 70, 1012.5)
