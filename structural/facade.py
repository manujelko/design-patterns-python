class Projector:
    def on(self) -> None:
        print("Projector turned on")

    def off(self) -> None:
        print("Projector turned off")


class SoundSystem:
    def activate_surround_sound(self) -> None:
        print("Surround sound activated")

    def deactivate_surround_sound(self) -> None:
        print("Surround sound deactivated")


class DVDPlayer:
    def play_movie(self, movie_title: str) -> None:
        print(f"Playing movie '{movie_title}'")

    def stop_movie(self) -> None:
        print("Stopped movie")


class HomeTheaterFacade:
    def __init__(
        self, projector: Projector, sound_system: SoundSystem, dvd_player: DVDPlayer
    ) -> None:
        self.projector = projector
        self.sound_system = sound_system
        self.dvd_player = dvd_player

    def watch_movie(self, movie_title: str) -> None:
        print("Get ready to watch a movie...")
        self.projector.on()
        self.sound_system.activate_surround_sound()
        self.dvd_player.play_movie(movie_title)

    def end_movie(self) -> None:
        print("Shutting movie theater down...")
        self.dvd_player.stop_movie()
        self.sound_system.deactivate_surround_sound()
        self.projector.off()


if __name__ == "__main__":
    projector = Projector()
    sound_system = SoundSystem()
    dvd_player = DVDPlayer()
    home_theater = HomeTheaterFacade(projector, sound_system, dvd_player)
    home_theater.watch_movie("The Matrix")
    home_theater.end_movie()
