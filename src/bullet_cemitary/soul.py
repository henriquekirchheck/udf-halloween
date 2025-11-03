from typing import Literal, override

import pygame

from bullet_cemitary.node import Node


class Soul(Node):
    _rect: pygame.Rect
    _accel: tuple[float, float] = (0, 0)

    @override
    def _init(self) -> None:
        self._rect = pygame.Rect(0, 0, 25, 25)

    @override
    def _process(self, delta: float) -> None:
        self._rect.move_ip(self._accel)

        _ = pygame.draw.rect(
            self.get_surface(),
            (255, 0, 0),
            self._rect,
        )

    @override
    def _process_physics(self) -> None:
        print(self._accel)

    @override
    def _event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            key: int = event.key  # pyright: ignore[reportAny]
            match key:
                case pygame.K_UP:
                    self._accel = (-1, self._accel[1])
                case pygame.K_DOWN:
                    self._accel = (1, self._accel[1])
                case pygame.K_LEFT:
                    self._accel = (self._accel[0], -1)
                case pygame.K_RIGHT:
                    self._accel = (self._accel[0], 1)
                case _:
                    pass
