import pygame


class Sprite(pygame.sprite.Sprite): ...


class Group[T: Sprite](pygame.sprite.AbstractGroup[T]): ...
