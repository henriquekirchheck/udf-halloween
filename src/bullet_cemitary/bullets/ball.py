from typing import final, override

import pygame

from bullet_cemitary.engine.asset_loader import load_image


@final
class Ball(pygame.sprite.Sprite):
    _speed: list[int]
    _bounding: tuple[int, int]

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = load_image("intro_ball.webp")
        self.rect: pygame.Rect = self.image.get_rect(center=(100, 100))
        self._speed = [2, 2]
        self._bounding = pygame.display.get_window_size()

    @override
    def update(self) -> None:
        self.rect.move_ip(self._speed)

        if self.rect.left < 0 or self.rect.right > self._bounding[0]:
            self._speed[0] = -self._speed[0]

        if self.rect.top < 0 or self.rect.bottom > self._bounding[1]:
            self._speed[1] = -self._speed[1]
