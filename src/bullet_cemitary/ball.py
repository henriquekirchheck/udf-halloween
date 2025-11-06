from typing import TYPE_CHECKING, final, override

import pygame

from bullet_cemitary.engine.asset_loader import load_image

if TYPE_CHECKING:
    from collections.abc import Callable


@final
class Ball(pygame.sprite.Sprite):
    _speed: tuple[int, int]
    _bounds: tuple[int, int]

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = load_image("intro_ball.webp")
        self.rect: pygame.Rect = self.image.get_rect()
        self._bounds = pygame.display.get_window_size()
        self._speed = 5, 5

    def set_bounds(self, w: int, h: int) -> None:
        self._bounds = w, h

    @override
    def update(self) -> None:
        self.rect = self.rect.move(self._speed)

        if self.rect.left < 0 or self.rect.right > self._bounds[0]:
            self._speed = -self._speed[0], self._speed[1]

        if self.rect.top < 0 or self.rect.bottom > self._bounds[1]:
            self._speed = self._speed[0], -self._speed[1]
