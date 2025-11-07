from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from collections.abc import Callable

    from bullet_cemitary.engine.scene import Scene

PHYSICS_EVENT: int = pygame.event.custom_type()


def run(scene_class: Callable[[pygame.Surface], Scene]) -> None:
    _ = pygame.init()
    clock = pygame.Clock()
    pygame.time.set_timer(PHYSICS_EVENT, int(1000 / 30))
    delta = 0.0

    screen = pygame.display.set_mode(
        (960, 720),
        pygame.SCALED,
    )

    scene = scene_class(screen)

    while True:
        for event in pygame.event.get():
            scene.event(event)
            if event.type == PHYSICS_EVENT:
                scene.physics_update()

        scene.update(delta)

        pygame.display.flip()

        delta = clock.tick() / 1000
