from typing import override

import pygame

from bullet_cemitary.node import Node

PHYSICS_EVENT = pygame.event.custom_type()


class App(Node):
    _display_surf: pygame.Surface
    _running: bool
    _size: tuple[int, int]
    _clock: pygame.time.Clock

    def __init__(self) -> None:
        super().__init__()
        _ = pygame.init()
        info = pygame.display.Info()
        self._size = info.current_w, info.current_h
        self._display_surf = pygame.display.set_mode(
            self._size,
            pygame.FULLSCREEN | pygame.DOUBLEBUF,
        )
        self._clock = pygame.time.Clock()

    @override
    def _init(self) -> None:
        pass

    @override
    def _process_physics(self) -> None:
        pass

    @override
    def _process(self, delta: float) -> None:
        pass

    @override
    def _event(self, event: pygame.event.Event) -> None:
        if event.type == PHYSICS_EVENT:
            self.process_physics()
        if event.type == pygame.QUIT:
            self._running = False

    def run(self) -> None:
        self._running = True
        pygame.time.set_timer(PHYSICS_EVENT, 200)

        delta = 0.0
        while self._running:
            self.process(delta)

            event = pygame.event.poll()
            if event.type != pygame.NOEVENT:
                self.event(event)

            pygame.display.flip()
            delta = self._clock.tick() / 1000

        pygame.time.set_timer(PHYSICS_EVENT, 0)

    @override
    def get_surface(self) -> pygame.Surface:
        return self._display_surf
