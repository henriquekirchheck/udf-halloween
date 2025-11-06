import math
from typing import Literal, final, override

import numpy as np
import pygame

from bullet_cemitary.engine.asset_loader import load_image

SQRT2 = math.sqrt(2)


@final
class SoulSprite(pygame.sprite.Sprite):
    health: int
    _directions = np.zeros(2)
    _slowed: bool = True
    _position = np.zeros(2)

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = load_image("soul/heart.webp", alpha=True)
        self.rect: pygame.Rect = self.image.get_rect()
        self.health = 20

    @override
    def update(self) -> None:
        speed = (0.5 if self._slowed else 1.0) * 8.0
        move = self._directions * speed
        if move[0] != 0 and move[1] != 0:
            move = move / SQRT2
        self._position += move
        self.rect.x = self._position[0]
        self.rect.y = self._position[1]

    def event(self, event: pygame.Event) -> None:
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            self._slowed = event.mod & pygame.KMOD_SHIFT  # pyright: ignore[reportAny]
            key: int = event.key  # pyright: ignore[reportAny]
            if event.type == pygame.KEYDOWN:
                if key == pygame.K_UP:
                    self._directions[1] += -1
                if key == pygame.K_DOWN:
                    self._directions[1] += 1
                if key == pygame.K_LEFT:
                    self._directions[0] += -1
                if key == pygame.K_RIGHT:
                    self._directions[0] += 1
            if event.type == pygame.KEYUP:
                if key == pygame.K_UP:
                    self._directions[1] -= -1
                if key == pygame.K_DOWN:
                    self._directions[1] -= 1
                if key == pygame.K_LEFT:
                    self._directions[0] -= -1
                if key == pygame.K_RIGHT:
                    self._directions[0] -= 1


@final
class GameOverSprite(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = load_image("soul/broken.webp", alpha=True)
        self.rect: pygame.Rect = self.image.get_rect()


@final
class ShardSprite(pygame.sprite.Sprite):
    def __init__(self, shard: Literal["1", "2", "3", "4"]) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface = load_image(
            f"soul/shards/{shard}.webp",
            alpha=True,
        )
        self.rect: pygame.Rect = self.image.get_rect()
