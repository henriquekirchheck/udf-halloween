from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, cast, final, override

import pygame

from bullet_cemitary.engine.asset_loader import load_image
from bullet_cemitary.engine.scene import Scene

if TYPE_CHECKING:
    from collections.abc import Iterator


@final
class BattleScene(Scene):
    selected: Literal[0, 1, 2, 3] = 0
    actions: Options
    soul: pygame.Surface
    soul_pos: pygame.Rect

    @override
    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)
        self.actions = load_options()

        margin = 32 * 2
        max_width = int(self.screen.width - margin)
        action_width = self.actions.get_total_width()
        leftover_space = max_width - action_width
        gap = leftover_space / 3
        for i, action in enumerate(self.actions):
            action.pos.x = (margin / 2) + (gap * i) + (action.pos.width * i)
            action.pos.bottom = self.screen.height - 5 * 2

        self.soul = load_image("soul/heart.webp", alpha=True)
        self.soul_pos = self.soul.get_rect()

        self.reset()

    def reset(self) -> None:
        self.selected = 0

    @override
    def update(self, delta: float) -> None:
        _ = self.screen.fill((0, 0, 0))
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
                case pygame.K_RIGHT if self.selected < 3:
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
        self.active = active
        self.inactive = inactive


@dataclass
class Options:
    fight: Option
    act: Option
    item: Option
    mercy: Option

    def get_options(self) -> tuple[Option, Option, Option, Option]:
        return self.fight, self.act, self.item, self.mercy

    def __iter__(self) -> Iterator[Option]:
        return self.get_options().__iter__()

    def get_total_width(self) -> int:
        return sum(x.pos.w for x in self.get_options())


def load_options() -> Options:
    return Options(
        fight=Option(
            inactive=load_image("encounter/fight.webp", alpha=True),
            active=load_image("encounter/fight_selected.webp", alpha=True),
        ),
        act=Option(
            inactive=load_image("encounter/act.webp", alpha=True),
            active=load_image("encounter/act_selected.webp", alpha=True),
        ),
        item=Option(
            inactive=load_image("encounter/item.webp", alpha=True),
            active=load_image("encounter/item_selected.webp", alpha=True),
        ),
        mercy=Option(
            inactive=load_image("encounter/mercy.webp", alpha=True),
            active=load_image("encounter/mercy_selected.webp", alpha=True),
        ),
    )
