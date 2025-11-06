import pathlib
from typing import LiteralString

import pygame

ASSET_DIR = pathlib.Path("assets")


def load_image(
    path: LiteralString,
    *,
    alpha: bool = False,
) -> pygame.Surface:
    asset = pygame.image.load(ASSET_DIR / path)
    return asset.convert_alpha() if alpha else asset.convert()


def load_audio(path: LiteralString) -> pygame.Sound:
    return pygame.mixer.Sound(ASSET_DIR / path)


def load_font(path: LiteralString) -> pygame.Font:
    return pygame.font.Font(ASSET_DIR / path)
