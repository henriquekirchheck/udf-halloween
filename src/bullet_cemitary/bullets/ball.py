from typing import final, override

import numpy as np
import pygame

from bullet_cemitary.bullets.sprite import BulletSprite
from bullet_cemitary.engine.asset_loader import load_image


@final
class Ball(BulletSprite):
    _speed = np.ones(2)
    _bounding: tuple[int, int]
    _position = np.zeros(2)

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = load_image("intro_ball.webp")

        self._position[:] = (100, 100)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = self._position[0]
        self.rect.y = self._position[1]

        self._speed *= 300
        self._bounding = pygame.display.get_window_size()

    @override
    def update(self, delta: float) -> None:
        self._position += self._speed * delta
        self.rect.x = self._position[0]
        self.rect.y = self._position[1]

        if self.rect.left < 0 or self.rect.right > self._bounding[0]:
            self._speed[0] = -self._speed[0]

        if self.rect.top < 0 or self.rect.bottom > self._bounding[1]:
            self._speed[1] = -self._speed[1]

    @property
    @override
    def damage(self) -> int:
        return 4
