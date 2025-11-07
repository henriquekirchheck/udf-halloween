from abc import ABC, abstractmethod

import pygame


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
