import typing
import pygame

from bullet_cemitary.entity import Entity


class App:
    _display_surf: pygame.Surface
    _running: bool
    _size: tuple[int, int]
    _clock: pygame.time.Clock

    _objects: list[Entity]

    def __init__(self) -> None:
        _ = pygame.init()
        info = pygame.display.Info()
        self._size = info.current_w, info.current_h
        self._display_surf = pygame.display.set_mode(
            self._size,
            pygame.HWSURFACE | pygame.DOUBLEBUF,
        )
        self._clock = pygame.time.Clock()
        self._objects = []
        self._running = True

    def run(self) -> None:
        delta = 0.0
        while self._running:
            for game_obj in self._objects:
                game_obj.process(delta)

            delta = self._clock.tick() / 1000
            print(delta)


def main() -> None:
    app = App()
    app.run()


if __name__ == "__main__":
    main()
