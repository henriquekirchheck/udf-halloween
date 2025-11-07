from dataclasses import dataclass
from typing import Literal, Self, cast, final, override

import pygame

from bullet_cemitary.engine.asset_loader import load_image
from bullet_cemitary.engine.scene import Scene


@final
class BattleScene(Scene):
    selected: Literal[0, 1, 2, 3] = 0

    @override
    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)
        self.actions = load_options()

        size = int(self.screen.width / 4)
        for i, action in enumerate(self.actions):
            action.pos.x = size * i

        self.soul = load_image("soul/heart.webp")
        self.reset()

    def reset(self) -> None:
        self.selected = 0

    @override
    def update(self, delta: float) -> None:
        for i, action in enumerate(self.actions):
            surf = action.active if i == self.selected else action.inactive
            _ = self.screen.blit(surf, action.pos)
            if i == self.selected:
                _ = self.screen.blit(self.soul, action.pos)

    @override
    def physics_update(self) -> None: ...

    @override
    def event(self, event: pygame.Event) -> None:
        if event.type == pygame.KEYDOWN:
            key: int = event.key  # pyright: ignore[reportAny]
            match key:
                case pygame.K_LEFT if self.selected > 0:
                    self.selected = cast("Literal[0, 1, 2]", self.selected - 1)
                case pygame.K_RIGHT:
                    self.selected = cast("Literal[1, 2, 3]", self.selected + 1)
                case _:
                    pass


@dataclass
class Option:
    active: pygame.Surface
    inactive: pygame.Surface
    pos: pygame.Rect

    def __init__(self, active: pygame.Surface, inactive: pygame.Surface) -> None:
        active_rect = active.get_rect()
        inactive_rect = inactive.get_rect()
        assert active_rect.w == inactive_rect.w, "w do not match between rects"
        assert active_rect.h == inactive_rect.h, "h do not match between rects"
        self.pos = inactive_rect


@dataclass
class Options:
    fight: Option
    act: Option
    item: Option
    mercy: Option

    def get_options(self) -> tuple[Option, Option, Option, Option]:
        return self.fight, self.act, self.item, self.mercy

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> Option:
        for option in self.get_options():
            return option
        raise StopIteration


def load_options() -> Options:
    return Options(
        fight=Option(
            inactive=load_image("encounter/fight.webp"),
            active=load_image("encounter/fight_selected.webp"),
        ),
        act=Option(
            inactive=load_image("encounter/act.webp"),
            active=load_image("encounter/act_selected.webp"),
        ),
        item=Option(
            inactive=load_image("encounter/item.webp"),
            active=load_image("encounter/item_selected.webp"),
        ),
        mercy=Option(
            inactive=load_image("encounter/mercy.webp"),
            active=load_image("encounter/mercy_selected.webp"),
        ),
    )
