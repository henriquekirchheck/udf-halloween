import pygame

from bullet_cemitary.bullets.sprite import BulletSprite


class BulletGroup(pygame.sprite.Group[BulletSprite]): ...
