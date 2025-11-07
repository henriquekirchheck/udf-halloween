from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from collections.abc import Callable


class Scene(ABC):
    screen: pygame.Surface

    @abstractmethod
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    @abstractmethod
    def update(self, delta: float) -> None: ...

    @abstractmethod
    def physics_update(self) -> None: ...

    @abstractmethod
    def event(self, event: pygame.Event) -> None: ...


PHYSICS_EVENT: int = pygame.event.custom_type()


def runner(scene_class: Callable[[pygame.Surface], Scene]) -> None:
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
