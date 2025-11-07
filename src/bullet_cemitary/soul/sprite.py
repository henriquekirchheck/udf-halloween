import math
from typing import TYPE_CHECKING, Literal, final, override

import numpy as np
import pygame

from bullet_cemitary.engine.asset_loader import load_audio, load_image
from bullet_cemitary.engine.sprite import Sprite

if TYPE_CHECKING:
    from bullet_cemitary.bullets.sprite import BulletSprite

SQRT2 = math.sqrt(2)


@final
class SoulSprite(Sprite):
    health: float
    _invencibility: int = 0
    _directions = np.zeros(2)
    _slowed: bool = False
    _position = np.zeros(2)

    _original: pygame.Surface
    _blink: pygame.Surface

    def __init__(self) -> None:
        Sprite.__init__(self)

        self._original = load_image("soul/heart.webp", alpha=True)

        self.image: pygame.Surface = self._original.copy()
        self.rect: pygame.Rect = self.image.get_rect()

        self._blink = pygame.Surface(self.rect.size)
        self._blink.set_colorkey((0, 0, 0))

        self._hurt = load_audio("soul/snd_hurt1.wav")

        self.health = 20

    @override
    def update(self, delta: float) -> None:
        speed = (0.5 if self._slowed else 1.0) * 250.0
        move = self._directions * speed
        if move[0] != 0 and move[1] != 0:
            move /= SQRT2

        self._position += move * delta
        self.rect.x = self._position[0]
        self.rect.y = self._position[1]

    @override
    def physics_update(self) -> None:
        if self._invencibility % 2:
            self.image = self._blink
        else:
            self.image = self._original

        if self._invencibility > 0:
            self._invencibility = self._invencibility - 1

    @override
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

    def collision(self, sprite: BulletSprite) -> None:
        if sprite.rect and self._invencibility == 0:
            self.health -= sprite.damage
            self._invencibility = 20
            _ = self._hurt.play()


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
