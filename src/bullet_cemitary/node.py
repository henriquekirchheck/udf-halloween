from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from pygame import Surface

if TYPE_CHECKING:
    import pygame


class Node(ABC):
    parent: Node | None = None
    children: list[Node]

    def __init__(
        self,
    ) -> None:
        """
        Please call `super().__init__()` as first thing in override.
        """
        self.children = []
        self.parent = None

    @abstractmethod
    def _init(self) -> None:
        return None

    @abstractmethod
    def _process(self, delta: float) -> None:
        return None

    @abstractmethod
    def _process_physics(
        self,
    ) -> None:
        return None

    @abstractmethod
    def _event(self, event: pygame.event.Event) -> None:
        return None

    def event(self, event: pygame.event.Event) -> None:
        self._event(event)
        for child in self.children:
            child.event(event)

    def process(self, delta: float) -> None:
        self._process(delta)
        for child in self.children:
            child.process(delta)

    def process_physics(
        self,
    ) -> None:
        self._process_physics()
        for child in self.children:
            child.process_physics()

    def add_children(self, node: Node) -> None:
        node.parent = self
        self.children.append(node)
        node._init()

    def remove_children(self, node: Node) -> None:
        node.parent = None
        self.children.remove(node)

    def get_surface(self) -> Surface:
        if self.parent:
            return self.parent.get_surface()
        return self.get_surface()
