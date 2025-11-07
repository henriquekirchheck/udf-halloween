import sys
from typing import final, override

import pygame

from bullet_cemitary.battle import BattleScene
from bullet_cemitary.engine import scene
from bullet_cemitary.engine.scene import Scene


@final
class Main(Scene):
    CHANGE_SCENE_EVENT = pygame.event.custom_type()

    scene: Scene

    @override
    def __init__(self, screen: pygame.Surface) -> None:
        super().__init__(screen)

        self.scene = BattleScene(self.screen)

    @override
    def update(self, delta: float) -> None:
        self.scene.update(delta)

    @override
    def physics_update(self) -> None:
        self.scene.physics_update()

    @override
    def event(self, event: pygame.Event) -> None:
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            case pygame.KEYDOWN if event.key == pygame.K_ESCAPE:  # pyright: ignore[reportAny]
                pygame.quit()
                sys.exit(0)

            case pygame.KEYDOWN if (
                event.key == pygame.K_RETURN and event.mod & pygame.KMOD_ALT  # pyright: ignore[reportAny]
            ):
                _ = pygame.display.toggle_fullscreen()

            case self.CHANGE_SCENE_EVENT:
                self.scene = event.scene  # pyright: ignore[reportAny]

            case _:
                pass

        self.scene.event(event)


def main() -> None:
    scene.runner(Main)


if __name__ == "__main__":
    main()
