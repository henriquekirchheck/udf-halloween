import sys
from typing import final, override

import pygame

from bullet_cemitary.battle import BattleScene
from bullet_cemitary.engine import runner
from bullet_cemitary.engine.scene import Scene


@final
class Main(Scene):
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
        self.scene.event(event)

        if (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_RETURN  # pyright: ignore[reportAny]
            and event.mod & pygame.KMOD_ALT  # pyright: ignore[reportAny]
        ):
            _ = pygame.display.toggle_fullscreen()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


def main() -> None:
    runner.run(Main)


if __name__ == "__main__":
    main()
